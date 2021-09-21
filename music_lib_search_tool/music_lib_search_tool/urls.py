"""music_lib_search_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from music_lib_search_tool.apps.core import views as core_views
from music_lib_search_tool.apps.music_collection_search import views as music_collection_search_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("js-settings/", core_views.js_settings, name="js_settings"),
    path('', music_collection_search_views.Search_View.as_view(), name='Search_View'),
]

