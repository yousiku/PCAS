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
    sea = request.GET['search'].replace(' ','')
    s = jieba.lcut(sea,cut_all=False)
    results = []
    for ss in s:
        keywords = Keywords.objects.filter(keywords__icontains=ss)
        results.append(keywords)
    res = list(set(results[0]).union(*results[1:]))
    products = {}
    for pro in res:
        products[pro] = pipeidu(pro.keywords,s)
    pros = sorted(products.iteritems(),key=lambda products:products[1],reverse=True)
    print pros
    return render(request,'results.html',{'pros':pros})

def pipeidu(str_keywords,list_fenci):
    cnt = 0
    for fenci in list_fenci:
        if fenci in str_keywords:
            cnt += 1
    return cnt