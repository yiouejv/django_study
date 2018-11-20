from django.db.models import F, Q, Count
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return HttpResponse('index')


def add(request):
    try:
        # 通过Entry
        author = Author.objects.create(name='MrWang', age=18, email='wangwc@163.com')
        print('ID:', author.id)
        print('name:', author.name)
        print('age:', author.age)
        print('email:', author.email)

        # 通过Entry对象的save()方法完成增加
        author = Author(name='魏老师', age=30, email='laowei@163.com')
        author.save()
        print('插入成功后返回的对象id为：', author.id)

        # 通过字典创建实体对象
        dic = {
            'name': 'xxx',
            'age':  20,
            'email': 'xx@126.com'
        }
        author = Author(**dic)
        author.save()
        print('xx的ID为:', author.id)
        return HttpResponse('添加成功')
    except Exception as err:
        print(err)
        return HttpResponse('添加失败')


def update_f(request):
    # 所有人的年龄加10
    Author.objects.all().update(age=F('age')+10)
    return HttpResponse('ok')


def query(request):
    # 查询id>=3 或 年龄小于60的信息
    authors = Author.objects.values().filter(Q(age__lte=60)|Q(id__gt=3))
    print(authors)
    return HttpResponse('okok')


def oto(reuqest):
    # 通过姓名为
    # '魏夫人'
    # wife信息查找对应的author，打印在终端上
    # 通过姓名为
    # '王老师'
    # wife信息查找对应的wife，打印在终端上
    author = Wife.objects.get(name='魏夫人').author
    print(author)

    wife = Author.objects.get(name='王老师').wife
    print('姓名：{name}, 年龄：{age}'.format(**wife.__dict__))
    return HttpResponse('ok')


def otm(request):
    publisher = Book.objects.get(id=3).publisher
    print(publisher)

    books = Publisher.objects.get(id=3).book_set.all()
    print(books)
    return HttpResponse('ok')


def mtm(request):
    publisher = Publisher.objects.get(id=3)
    print(publisher)
    authors = publisher.authors.all()
    print(authors)

    author = Author.objects.get(id=8)
    print(author)
    publishers = author.publisher_set.all()
    print(publishers)

    n = Author.objects.author_count()
    print(n)

    authors = Author.objects.age_filter(19).values()
    print(authors)

    books = Book.objects.filter_book('flask')
    print(books)
    return HttpResponse('ok')