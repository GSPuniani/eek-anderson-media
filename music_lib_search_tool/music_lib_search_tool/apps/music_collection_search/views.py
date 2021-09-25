from django.shortcuts import render
from django.views import View
from django.db import connection

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

    def get(self, request):
        context = {}
        return render(request, 'music_collection_search/Search_View.html', context)