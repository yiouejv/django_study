# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-16 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_study_4', '0002_auto_20181116_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('publicate_date', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['age', '-id'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
    ]
