from django.core import serializers
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
from django.views.decorators.csrf import csrf_protect


def index(request):
    return HttpResponse('index')


def request(request):
    print(request)
    context = {
        'scheme': request.scheme,
        'body': request.body,
        'path': request.path,
        'full_path': request.get_full_path(),
        'host': request.get_host(),
        'method': request.method,
        'post': request.POST,
        'get': request.GET,
        'cookies': request.COOKIES,
        'meta': request.META,
    }
    return render(request, 'five_day/request.html', context)


def request2(request):
    args = request.GET
    print('年:', args.get('year', '10000年'))
    print('月:', args.get('month'))
    print('日:', args.get('day'))
    return HttpResponse('xxx')


def post(request):
    if request.method == 'POST':
        # csrf_token = request.POST.get['csrfmiddlewaretoken']
        print(request.POST)
        print('xxx')
        return HttpResponse('post')
    else:
        return render(request, 'five_day/post.html')


def form(request):
    if request.method == 'GET':
        form = RemarkForm()
        context = {
            'form': form,
        }
        return render(request, 'five_day/form.html', context)
    else:
        # form = request.POST
        form = RemarkForm(request.POST)
        if form.is_valid():
            subject = form.get('subject')
            email = form.get('email')
            message = form.get('message')
            topic = form.get('topic')
            is_save = bool(form.get('is_save'))
            print(is_save)
            print(type(is_save))
            remark = Remark(subject=subject, email=email, message=message,
                            topic=topic, is_save=is_save)
            remark.save()
            print(remark.__dict__)
        return HttpResponse('xxx')


def register(request):
    if request.method == 'GET':
        return render(request, 'five_day/register.html')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            forms = request.POST
            name = forms.get('name')
            age = forms.get('age')
            email = forms.get('email')
            user = User(name=name, age=age, email=email)
            user.save()
            HttpResponse().delete_cookie()
            return HttpResponse('ok')
        else:
            return HttpResponse('fail')


def remake(request):
    remakes = Remark.objects.all()
    print(remakes)
    json_remakes = serializers.serialize('json', remakes)
    return HttpResponse(json_remakes)


def ajax(request):
    return render(request, 'remakes.html')