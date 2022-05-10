from cProfile import label
from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from coolC.models import Measure
from coolC.serializers import MeasureSerializer
import requests, json
import datetime                            # Imports datetime library
import pickle
import pymongo
from pymongo import MongoClient
import nazox.utils as uti

uri = 'localhost:27017'
client = MongoClient(uri)
db=client.coolC
collection=db.coolC_measure
collection2=db.coolC_measure_moy
collection3=db.coolC_measure_moy_hour
collection4=db.coolC_measure_stats
#loaded_model = pickle.load("ml_models/finalized_model.pkl")

def statsByDate(request,date):
    print(date)
    if( date==None):
        date="20210811"
    date=date[:4]+"-"+date[4]+date[5]+"-"+date[-2:]
    print(date)
    if request.method=='GET':
        measures=collection4.find({'Date': date})
        print(measures.count())
        count=measures.count()
        labels = []
        hours = []
        dataMoy = []
        dataMin = []
        dataMax = []
        mvt=[]
        for item in measures:
            labels.append(item['Date'])
            hours.append(item['Time'])
            mvt.append(item['Mvt'])
            dataMoy.append(item['Moy'])
            dataMin.append(item['Min'])
            dataMax.append(item['Max'])
        hours=list(set(hours))
        return JsonResponse(data={
                'count':count,
                'labels': labels,
                'hours':hours,
                'mvt':mvt,
                'dataMoy': dataMoy,
                'dataMin': dataMin,
                'dataMax': dataMax,
                }
                ,safe=False
            )
@csrf_exempt
def measureApi(request,id=0):
    if request.method=='GET':
        measures = Measure.objects.all()[:10]  
        measures_serializer=MeasureSerializer(measures,many=True)
        return JsonResponse(measures_serializer.data,safe=False)
    elif request.method=='POST':
        measure_data=JSONParser().parse(request)
        measures_serializer=MeasureSerializer(data=measure_data)
        if measures_serializer.is_valid():
            measures_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        measure_data=JSONParser().parse(request)
        measure=Measure.objects.get(measureId=measure_data['measureId'])
        measures_serializer=MeasureSerializer(measure,data=measure_data)
        if measures_serializer.is_valid():
            measures_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        measure=Measure.objects.get(measureId=id)
        measure.delete()
        return JsonResponse("Deleted Successfully",safe=False)

def averageByDate(request):
    if request.method=='GET':
        measures=collection2.find()
        print("--------------------------------")
        print(measures.count())
        count=measures.count()
        data=measures[0]['Temp']
        print("***************************")
        labels = []
        data = []
        for item in measures:
            labels.append(item['Date'][-5:])
            data.append(item['Temp'])
        return JsonResponse(data={
                'count':count,
                'labels': labels,
                'data': data,
                }
                ,safe=False
            )

def measuresByDate(request,date="2021-08-10"):
    if request.method=='GET':
        measures=collection3.find({'Date': date}).sort("_id",-1).limit(50)
        print("--------------------------------")
        print(measures.count())
        count=measures.count
        data=measures[0]['Temp']
        print("***************************")
        labels = []
        data = []
        for item in measures:
            labels.append(item['Time'])
            data.append(item['Temp'])
        return JsonResponse(data={
                'count':count,
                'labels': labels,
                'data': data,
                }
                ,safe=False
            )

def measuresCount():
    count=collection.find().count()
    return JsonResponse(data={
                'count':count,
                }
                ,safe=False
            )

def measuresByMonth(request,month):
    if request.method=='GET':
        measures=collection.find({'Date': {'$regex': '-'+month+'-'}})
        #measures = collection.find({"Date": '/(-'+month+'-)/'}).limit(10)  
        print("--------------------------------")
        print(measures.count())
        measures_serializer=MeasureSerializer(measures,many=True)
        return JsonResponse(measures_serializer.data,safe=False)

def last(id=0):
    measures = collection.find().sort("_id",-1).limit(2)  
    measures_serializer=MeasureSerializer(measures,many=True)
    return JsonResponse(measures_serializer.data,safe=False)

def weather(id=0):
    api_key = "d4fd671fd7718366348667d36c6c77a2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Ariana,Tunisia"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name+"&units=metric"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        return JsonResponse(x)
    else:
	    print(" City Not Found ")
