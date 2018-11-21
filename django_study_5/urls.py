#encoding: utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', index),
    url('^request/$', request),
    url('^request2/$', request2),
    url('^post/$', post),
    url('^form/$', form),
    url('^register/$', register),
    url('^remakes/$', remake),
    url('^ajax/$', ajax),
]