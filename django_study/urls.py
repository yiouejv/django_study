"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 当访问路径的url前缀为django_study_1/时, 提交到django_study_1下的urls去匹配
    url(r'^django_study_1/', include('django_study_1.urls')),
    url(r"^django_study_2/", include('django_study_2.urls')),
    url(r'^django_study_3/', include('django_study_3.urls')),
    url(r'^django_study_4/', include('django_study_4.urls')),
]


