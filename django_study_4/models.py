from django.db import models

# Create your models here.
from django.db.models import Count


class AuthorManager(models.Manager):
    def author_count(self):
        return self.aggregate(Count('id'))

    def age_filter(self, age_f):
        '''
            返回年龄小于指定年龄的结果集
        :param age_f: 指定年龄
        :return: 结果集
        '''
        return self.filter(age__lt=age_f).all()


class Author(models.Model):
    objects = AuthorManager()
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        # 指定映射到表的名称
        # db_table = 'author'

        # 定义在后台的显示名称(单数)
        verbose_name = '作者'

        # 定义在后台的显示名称(复数)
        verbose_name_plural = verbose_name

        # 定义数据在后台的排序规则
        ordering = ['age', '-id']


class Publisher(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    address = models.CharField(max_length=200, verbose_name='地址')
    city = models.CharField(max_length=50, verbose_name='城市')
    country = models.CharField(max_length=50, verbose_name='国家')
    website = models.URLField(verbose_name='主页')
    authors = models.ManyToManyField(Author, verbose_name='签约作者')

    class Meta():
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.name


class BookManager(models.Manager):
    def filter_book(self, r):
        '''
            筛选出只包含指定字符的结果集
        :param r: 指定字符
        :return: 结果集
        '''
        return self.filter(title__contains=r).all()


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=20, verbose_name='书名')
    publicate_date = models.DateField(verbose_name='发布日期')

    # 建立多对一关系
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', null=True)
    authors = models.ManyToManyField(Author)

    class Meta():
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['-publicate_date',]

    def __str__(self):
        return '%s' % self.title


class Wife(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    class Meta():
        verbose_name = 'wife'
        verbose_name_plural = verbose_name

    author = models.OneToOneField(Author, null=True, verbose_name='husband')


