#encoding: utf-8

from django.conf.urls import url
from .views import *

# 定义django_study_1/ 下的url
urlpatterns = [
    url(r'^index/$', index),
    # http://127.0.0.1:8000/01-show, 交给show_view 的视图处理
    url(r'^01-show/$', show_view),
    # 访问地址 http://127.0.0.1:8000/02-show/四位数字, 交给show02_views去处理
    url(r"^02-show/(\d{2,4})/$", show02_view),

    # 输出生日
    url(r"^03-show/(\d{4})/(\d{1,})/(\d{1,})/$", show03_view),

    # url传参
    url(r"^04-show/$", show04_view, {
        'name': 'haseke',
        'age': 15,
    }),
]