#encoding: utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', index),
    url('^index/$', index),
    url('^add/$', add),
    url('^update_f/$', update_f),
    url('^query/$', query),
    url('^oto/$', oto),
    url('^otm/$', otm),
]