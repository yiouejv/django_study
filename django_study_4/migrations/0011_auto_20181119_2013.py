# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-19 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_study_4', '0010_publisher_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wife',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_study_4.Author', verbose_name='husband'),
        ),
    ]
