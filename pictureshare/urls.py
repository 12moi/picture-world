from django.conf.urls import re_path
from . import views
from  django.conf.urls.static import static


urlpatterns=[
    re_path(r'^', views.index, name='',),

]