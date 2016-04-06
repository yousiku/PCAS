#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Keywords

# Create your views here.
def index(request):
    string = "helloworld"
    return render(request,'index.html',{'string':string})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def search(request):
    sea = request.GET['search']
    keywords = Keywords.objects.all()
    for key in keywords:
        print key.skuid
    return HttpResponse(sea)