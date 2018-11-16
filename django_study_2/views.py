from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "two_day/index.html")


def show_test(request):
    return HttpResponse('test')


def show_test02(request, num):
    return HttpResponse("传递进来的参数为："+ num)


def show_message():
    return 'this is a function'


class Dog(object):
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def eat(self):
        return self.name + '吃狗粮'


def var(request):
    context = {
        'name': '王老师',
        'age': 30,
        'gender': '男',
        "message": '天下没有吃不散的宴席',
        'tuple': ('王老师', 'MrRang', 'Rap Wang'),
        'list': ['!!!!!', '@@@@@', '#####'],
        'dic': {
            'bj': '北京',
            'sy': '沈阳',
            'cc': '长春',
        },
        'show_message': show_message,
        'dog': Dog(name='旺财'),
        'lst': [1, 2, 3, 4, 5, 6]
    }
    return render(request, "two_day/var.html", context)


def static(request):
    return render(request, "two_day/static_images.html")























