import json
from music_lib_search_tool.apps.music_collection_search.models import Genre, Instrument, Mood
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from music_lib_search_tool.apps.music_collection_search import csv_cleaner
from django.db import connection
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.conf import settings

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import MultiSearch, Search

from music_lib_search_tool.apps.music_collection_search.models import Song

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def run_db_query(query, args):
    with connection.cursor() as cursor:
        cursor.execute(query, args)
        result = dictfetchall(cursor)
    return result


class Search_View(View):

    def get(self, request):
        context = {}
        context['songs'] = Song.objects.order_by(F("overall_quality").desc(nulls_last=True)).all()[:10]
        context['genres'] = Genre.objects.order_by("name").all()
        context['instruments'] = Instrument.objects.order_by("name").all()
        context['moods'] = Mood.objects.order_by("name").all()

        return render(request, 'music_collection_search/Search_View.html', context)

class Database_View(View):

    def get(self, request):
        context = {"payload": csv_cleaner.build()}
        return render(request, 'music_collection_search/Database_View.html', context)

class Search_Test_View(View):

    def get(self, request):
        # query = request.GET.dict()['q']
        # query = query.split(' ')
        # print(query)

        # client = Elasticsearch()

        # s = Search().using(client).query("term", title=query)
        
        # ms = MultiSearch(index='song')

        # ms = ms.add(Search().using(client).filter('terms', title=query))
        # ms = ms.add(Search().using(client).filter('terms', description=query))
        # ms = ms.add(Search().using(client).filter('terms', description=query))
        # ms = ms.add(Search().using(client).filter('terms', description=query))


        # responses = ms.execute()

        # for hit in s:
        #     print(hit.title)
        
        responses = settings.ES.search(index="song", body={
            "query": {
                "combined_fields": {
                    "fields":["title", "description", "moods"],
                    "query": "this is a test",
                    "operator": "or",
                    "zero_terms_query": "all"
                }
            }
        })
        id_list = []
        for response in responses['hits']['hits']:
            id_list.append(response['_source']['id'])

        songs = Song.objects.filter(pk__in=id_list).all()
        print(songs)

        return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class Search_Results_View(View):

    def post(self, request, offset):
        query = request.POST.dict()['q']

        genres_id_list = []
        moods_id_list = []
        instruments_id_list = []
        if request.POST.dict()['genres'] != "null":
          genres_id_list = [int(x) for x in request.POST.dict()['genres'].strip('][').split(',')]
        if request.POST.dict()['moods'] != "null":  
          moods_id_list = [int(x) for x in request.POST.dict()['moods'].strip('][').split(',')]
        if request.POST.dict()['instruments'] != "null":  
          instruments_id_list = [int(x) for x in request.POST.dict()['instruments'].strip('][').split(',')]
        bpm_low = int(request.POST.dict()['bpm_low'])
        bpm_high = int(request.POST.dict()['bpm_high'])
        print(request.POST.dict()['genres'])
        print(genres_id_list)
        print([ { "term": { "genre_ids": str(i) }} for i in genres_id_list ])
        responses = settings.ES.search(index="song", body={
            "from": offset*10,
            "size": 10,
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "title": {
                                    "query": query,
                                    "boost": 300
                                }
                            }
                        },
                        {
                            "match": {
                                "description": {
                                    "query": query,
                                    "boost": 200
                                }
                            }
                        },
                        {
                            "match": {
                                "keywords": {
                                    "query": query,
                                    "boost": 100
                                }
                            }
                        }
                    ],
                    "must" : {
                        "bool" : {
                            "should" : 
                            [{
                                "match" : {
                                    "genre_ids": str(i)
                                }
                            } for i in genres_id_list],
                            "minimum_should_match": 1
                        }
                    }
                },
             },
        })

        id_list = []
        song_list = []
        for response in responses['hits']['hits']:
            id_list.append(response['_source']['id'])
            song_list.append(Song.objects.filter(id=response['_source']['id']).first())


        data = {
            'num':len(song_list),
            'keywords':query,
            'songs': [song.to_dict() for song in song_list]
        }
        return JsonResponse(json.dumps(data), status=200, safe=False)

