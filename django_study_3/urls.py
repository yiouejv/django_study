#encoding: utf-8
from .views import *
from django.conf.urls import url

urlpatterns = [
    url('^$', index),
    url('^index/$', index),
    url('^add/$', add),
    url('^query/$', query),
    url('^get/$', get),
    url('^update$', update),
    url('^delete/(\w*)?/$', delete, name='delete'),
    url('^queryall/$', queryall),
]