#encoding: utf-8

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^$", index),
    url(r"^index/$", index),

    # http://127.0.0.1:8000/django_study_2/test/
    url(r'^test/$', show_test),

    # http://127.0.0.1:8000/diango_study_2/test/四位数字
    url(r'^test/(\d{4})/$', show_test02),

    url(r'^var/$', var),

    url(r'^static/$', static),
]
