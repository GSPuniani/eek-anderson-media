import json
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
        context = {}
        return render(request, 'music_collection_search/Search_View.html', context)

class Database_View(View):

    def get(self, request):
        context = {"payload": csv_cleaner.get_song_titles()}
        return render(request, 'music_collection_search/Database_View.html', context)
      
class Search_Results_View(View):

    def get(self, request, offset):
        query = request.GET.dict()['q']
        keywords = query.split(' ')
        song_id_set = set()
        offset=offset*10

        sql = '''
        select search_keywords as id from search_keywords(%s) limit 10
        '''
        song_sql_result = run_db_query(sql, [keywords])
        print(song_sql_result[0]['id'])
        id_list = song_sql_result[0]['id'][offset:offset+10]
        print('Get Song Objects')
        song_list = Song.objects.filter(pk__in=id_list).all()
        
        data = {
            'num':len(song_list),
            'keywords':keywords,
            'songs': [song.to_dict() for song in song_list]
        }

        return JsonResponse(json.dumps(data), status=200, safe=False)

