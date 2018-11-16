from django.db import models

# Create your models here.


class TestModel(models.Model):
    test1 = models.CharField(max_length=20)
    test2 = models.CharField(max_length=30)
    test3 = models.FloatField()


class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()