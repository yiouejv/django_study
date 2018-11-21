from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')


class Remark(models.Model):
    subject = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    topic = models.IntegerField()
    is_save = models.BooleanField(default=True)


class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    email = models.EmailField()
