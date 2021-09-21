from django.shortcuts import render
from django.views import View
from .csv_cleaner import get_song_titles



class Search_View(View):

    def get(self, request):
        context = {}
        return render(request, 'music_collection_search/Search_View.html', context)

class Database_View(View):

    def get(self, request):
        context = {"payload": get_song_titles()}
        return render(request, 'music_collection_search/Database_View.html', context)