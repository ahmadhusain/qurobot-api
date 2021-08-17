from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import APISerializer, PerawiSerializer
from .models import Datamaster
from django.http import Http404
import pandas as pd

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Mencari hadis berdasarkan Imam Perawi dan Nomornya ':'/hadis/<str:ImamPerawi>/<str:no>',
        'Mencari hadis berdasarkan topik tertentu':'/carihadis/<str:keyword>',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def perawi(request):
    api_urls = {
        'Perawi': [
        'Imam Abu Daud',
        'Imam Bukhari',
        'Imam Musmlim',
        'Imam Ahmad',
        'Imam An-Nasa`i',
        'Imam Ibnu Majah',
        'Imam Malik',
        'Imam Tirmidzi'
        ]
    }
    return Response(api_urls)

@api_view(['GET'])
def hadis(request, imam, no):
    try:
        data = Datamaster.objects.filter(perawi=imam, number=no)
    except Datamaster.DoesNotExist:
        raise Http404("Hadits does not exist")
    serializer = APISerializer(data, many = True)
    to_json = {
        'code': 200,
        'message': 'HR. ' + imam + ' No. ' + no,
        'data':serializer.data
        }
    return Response(to_json)

@api_view(['GET'])
def carihadis(request, keyword):
    temp = Datamaster.objects.all()
    data = temp.filter(indonesia__contains=keyword).order_by('?')[:5]
    try:
        serializer = APISerializer(data, many = True)
        to_json = {
        'code': 200,
        'data':serializer.data
        }
    except Exception:
        to_json = {
        'error': 404
        }
    return Response(to_json)
    # return HttpResponse(serializer.data,content_type="application/json")