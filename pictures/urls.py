

from django.conf.urls import re_path
from . import views




urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^search/', views.search_results, name='search'),
    re_path(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]