from json import JSONEncoder
import json
from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from coolC.views import last, measuresCount, weather, statsByDate
import nazox.utils as uti
# Dashboard
class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        data=uti.from_Byte_toJson(last())
        weath=uti.from_Byte_toJson(weather())
        count=uti.from_Byte_toJson(measuresCount())
        #prediction=uti.from_Byte_toJson(predict())
        #print(request.session)
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Cool@-C"  
        greeting['previousTmp']=data[0]['Temp']
        greeting['currentTmp']=data[1]['Temp']
        greeting['Diffdegrees']=int(data[0]['Temp'])-int(data[1]['Temp'])
        state=uti.diff(int(data[0]['Temp'])-int(data[1]['Temp']))
        greeting['state']=state[0]
        greeting['menu']=state[1]
        greeting['badgeColor']=state[2]

        greeting['ExtTemp']=weath['main']['temp']
        greeting['weatherDesc']=weath['weather'][0]['description']
        greeting['weatherIcon']=uti.weatherState(weath['weather'][0]['main'])
        greeting['address']=weath['sys']['country']+", "+weath['name']

        greeting['count']=count['count']
        greeting['prediction']=uti.predict(int(weath['main']['temp']))
        
        return render(request, 'menu/index.html',greeting)
    

class RealTimeView(LoginRequiredMixin,View):
    def get(self,request):
        count=uti.from_Byte_toJson(measuresCount())
        greeting={}
        greeting['title'] = "Realtime"
        greeting['pageview'] = "RealTime"
        greeting['count']=count['count']
        return render(request,'charts/realtime.html',greeting) 
