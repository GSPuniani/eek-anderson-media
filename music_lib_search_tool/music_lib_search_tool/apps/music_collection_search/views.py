import json
from music_lib_search_tool.apps.music_collection_search.models import Genre, Instrument, Mood
from django.shortcuts import render
from django.views import View
from music_lib_search_tool.apps.music_collection_search import csv_cleaner
from django.db import connection
from django.http import JsonResponse


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
        q1 = Song.objects.all()[:15]
        context = {"test_data" : q1} # When the Search_View is called, DTL will make 3 identical songs
        return render(request, 'music_collection_search/Search_View.html', context)

class Database_View(View):

    def get(self, request):
        context = {"payload": csv_cleaner.get_song_titles()}
        return render(request, 'music_collection_search/Database_View.html', context)
      
class Search_Results_View(View):

    def get(self, request, offset):
        query = request.GET.dict()['q']
        keywords = query.split(' ')
        genres_id_list = request.GET.dict()['genres']
        moods_id_list = request.GET.dict()['moods']
        instruments_id_list = request.GET.dict()['instruments']
        offset=offset*10

        sql = '''
        select search_keywords as id from search_keywords(%s) limit 10
        '''
        song_sql_result = run_db_query(sql, [keywords])
        print(song_sql_result[0]['id'])
        id_list = song_sql_result[0]['id'][offset:offset+10]
        print('Get Song Objects')
        
        genre_list = Genre.objects.filter(pk__in=genres_id_list).all()
        mood_list = Mood.objects.filter(pk__in=moods_id_list).all()
        instrument_list = Instrument.objects.filter(pk__in=instruments_id_list).all()
        song_list = Song.objects.filter(pk__in=id_list, 
            genre__in=genre_list, 
            mood__in=mood_list, 
            instrument__in=instrument_list).all()
        
        data = {
            'num':len(song_list),
            'keywords':keywords,
            'songs': [song.to_dict() for song in song_list]
        }

        return JsonResponse(json.dumps(data), status=200, safe=False)

