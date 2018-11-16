from django.db.models import Sum, Avg
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


def query(request):
    authors = Author.objects.all()
    authors = Author.objects.all().values('name', 'email')
    for author in authors:
        print(author.get('name'))
        print(author.get('email'))

    # 通过values_list() 查询部分列的数据
    authors = Author.objects.values_list('name', 'email')
    print('authors', authors)

    # 首先按age降序排序，再按id升序排序
    authors = Author.objects.all().order_by('-age', 'id').values()
    for author in authors:
        print(author)

    # 通过django的orm，查询出Author实体中，年龄大于平均年龄的人的信息
    avgAge = Author.objects.aggregate(Avg('age'))['age__avg']
    authors = Author.objects.values().filter(age__gte=avgAge)
    print(authors)
    return HttpResponse('查询成功')


def get(request):
    # 通过get方法查询一条数据
    author = Author.objects.values().get(id=1)
    print(author)

    # 查询age 大于等于30的ahtuor的信息
    authors = Author.objects.values().filter(age__gte=30)
    print(authors)

    # 查询出age 小于等于30的author的信息
    authors = Author.objects.values().filter(age__lte=30)
    print('age 小于等于30的author的信息:', authors)

    # 查询出所有姓王的人的author信息
    authors = Author.objects.values().filter(name__startswith='王')
    print('所有姓王的人的author信息', authors)

    # 查询出所有email包含wang的author的信息
    authors = Author.objects.values().filter(email__contains='wang')
    print('所有email包含wang的author的信息:', authors)

    # 查询出所有publicate_date的时间在2005年的Book的信息
    books = Book.objects.values().filter(publicate_date__year='2015')
    print(books)

    # 查询出所有publishcate__date的时间在2015年以后的book的信息
    books = Book.objects.values().filter(publicate_date__year__gte='2015')
    print(books)

    # 查询author中年纪的总和
    age_sum = Author.objects.values().aggregate(Sum('age'))
    print(age_sum)

    # 按age进行分组查询所有的信息
    res = Author.objects.values('age').annotate(sumAge=Sum('age'))
    print(res)

    # 按名字进行分组，平均年龄大于20的所有信息
    authors = Author.objects.values('name').annotate(avgAge=Avg('age')).filter(avgAge__gte=20)
    print(authors)
    return HttpResponse('ok')


def update(request):
    # 将MrWang更改为RapWang
    authors = Author.objects.filter(name='MrWang')
    for author in authors:
        author.name = 'RapWang'
        author.save()

    # 将RapWang 更改为 MrWw
    Author.objects.filter(name='RapWang').update(name='MrWW')
    return HttpResponse('update')


def delete(request, id):
    Author.objects.get(id=id).delete()
    return HttpResponse('ok')


def queryall(request):
    authors = Author.objects.all().values()
    context = {
        'authors': authors
    }
    return render(request, "three_day/viewall.html", context)
