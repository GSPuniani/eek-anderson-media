from django.shortcuts import render
from django.views import View



class Search_View(View):

    def get(self, request):
        context = {}
        return render(request, 'music_collection_search/Search_View.html', context)        