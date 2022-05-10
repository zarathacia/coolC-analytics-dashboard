from ast import Param
from django.conf.urls import url
from coolC import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^measure$',views.measureApi,name="measures"),
    url(r'^measure/([0-9]+)$',views.measureApi),
    url(r'last',views.last),
    url('weather',views.weather),
    url(r'^month/([0-9]{2})',views.measuresByMonth),
    url('day/<str:date>',views.measuresByDate),
    url('avg',views.averageByDate),
    url(r'^stats$',views.statsByDate),
    url(r'^stats/([0-9]{8})',views.statsByDate),
    

    url(r'^realtime/measure$',views.measureApi,name="measures"),
    url(r'^realtime/measure/([0-9]+)$',views.measureApi),
    url(r'realtime/last',views.last),
    url('realtime/weather',views.weather),
    url(r'^realtime/month/([0-9]{2})',views.measuresByMonth),
    url('realtime/day/<str:date>',views.measuresByDate),
    url('realtime/avg',views.averageByDate),
    url(r'^realtime/stats$',views.statsByDate),
    url(r'^realtime/stats/([0-9]{8})',views.statsByDate),
    
]