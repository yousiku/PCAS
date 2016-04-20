#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Keywords
import jieba

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
    s = jieba.cut(sea,cut_all=False)
    results = []
    for ss in s:
        keywords = Keywords.objects.filter(keywords__icontains=ss)
        results.append(keywords)
    res = list(set(results[0]).intersection(*results[1:]))
    return render(request,'results.html',{'res':res})

