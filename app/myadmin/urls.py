# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from app.myadmin import views

urlpatterns = [
    url(r'^$', views.admin_index),
    url(r'^goods/$', views.admin_goods),
    url(r'^goodsclass/(\d*)$', views.admin_goodsclass),
    # url(r'^goodsclassedit/$', views.admin_goodsclassedit),
    url(r'^user/$', views.admin_user),
]
