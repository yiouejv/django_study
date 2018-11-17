from django.db import models

# Create your models here.

class Author(models.Model):
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

    class Meta():
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=20, verbose_name='书名')
    publicate_date = models.DateField(verbose_name='发布日期')

    # 建立多对一关系
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', null=True)

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

    author = models.OneToOneField(Author, null=True, verbose_name='husband  ')


