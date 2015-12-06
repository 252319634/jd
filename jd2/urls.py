# coding=utf-8
"""jd2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from app import myadmin
from app import views

urlpatterns = [
    url(r'^myadmin/', include(myadmin.urls)),
    url(r'^index/', views.index),
    url(r'^$', views.index),
    url(r'^verify/', views.verify),  # 这个没有$,后面要加随机数字
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^order/$', views.order),
    url(r'^address/$', views.address),
    url(r'^goods/$', views.goods),
    url(r'^list/$', views.list),
    url(r'^user/$', views.user),
    url(r'^flow1/$', views.flow1),
    url(r'^flow2/$', views.flow2),
    url(r'^flow3/$', views.flow3),
]
