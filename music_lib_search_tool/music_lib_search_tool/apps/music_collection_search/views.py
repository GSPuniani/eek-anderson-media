import json
from music_lib_search_tool.apps.music_collection_search.models import Genre, Instrument, Mood
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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
        context['genres'] = Genre.objects.all()
        context['instruments'] = Instrument.objects.all()
        context['moods'] = Mood.objects.all()
        return render(request, 'music_collection_search/Search_View.html', context)

class Database_View(View):

    def get(self, request):
        context = {"payload": csv_cleaner.get_song_titles()}
        return render(request, 'music_collection_search/Database_View.html', context)
    
@method_decorator(csrf_exempt, name='dispatch')
class Search_Results_View(View):

    def post(self, request, offset):
        query = request.POST.dict()['q']
        keywords = query.split(' ')
        genres_id_list = [int(x) for x in request.POST.dict()['genres'].strip('][').split(',')]
        moods_id_list = [int(x) for x in request.POST.dict()['moods'].strip('][').split(',')]
        instruments_id_list = [int(x) for x in request.POST.dict()['instruments'].strip('][').split(',')]
        bpm_low = int(request.POST.dict()['bpm_low'])
        bpm_high = int(request.POST.dict()['bpm_high'])
        offset=offset*10

        sql = '''
        select search_keywords as id from search_keywords(%s) limit 10
        '''

        song_sql_result = run_db_query(sql, [keywords])
        id_list = set(song_sql_result[0]['id'])

        genre_list = Genre.objects.filter(pk__in=genres_id_list).all()
        mood_list = Mood.objects.filter(pk__in=moods_id_list).all()
        instrument_list = Instrument.objects.filter(pk__in=instruments_id_list).all()

        song_list = Song.objects.filter(pk__in=id_list, bpm__lte=bpm_high, bpm__gte=bpm_low)\
            .filter(genre__in=genre_list, mood__in=mood_list, instrument__in=instrument_list)\
            .all()

        song_list = list(set(song_list))[offset:offset+10]
        print('Filter Applied')
        print(song_list)
        data = {
            'num':len(song_list),
            'keywords':keywords,
            'songs': [song.to_dict() for song in song_list]
        }
        return JsonResponse(json.dumps(data), status=200, safe=False)

