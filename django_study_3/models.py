from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Book(models.Model):
    title = models.CharField(max_length=20)
    publicate_date = models.DateField()