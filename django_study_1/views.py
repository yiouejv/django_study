from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('index')


def show_view(request):
    return HttpResponse('这是我的第一个django程序')


def show02_view(request, arg):
    return HttpResponse(arg)


def show03_view(request, year, month, day):
    return HttpResponse("生日为: %s年%s月%s日" % (year, month, day))


def show04_view(request, **kwargs):
    name = kwargs['name']
    age = kwargs['age']
    return HttpResponse("name: %s, age: %d" % (name, age))
