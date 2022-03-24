from django.conf.urls import path
from . import views
from  django.conf.urls.static import static


urlpatterns=[
    path(r'^', views.index, name='index',),

]