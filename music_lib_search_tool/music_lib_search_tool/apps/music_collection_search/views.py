from django.shortcuts import render
from django.views import View
from music_lib_search_tool.apps.music_collection_search import csv_cleaner



class Search_View(View):

    def get(self, request):
        context = {}
        return render(request, 'music_collection_search/Search_View.html', context)

class Database_View(View):

    def get(self, request):
        context = {"payload": csv_cleaner.get_song_titles()}
        return render(request, 'music_collection_search/Database_View.html', context)