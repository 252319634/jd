# coding=utf-8

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from app import myadmin
from app import views
from jd2 import settings

urlpatterns = [
    url(r'^myadmin/', include(myadmin.urls)),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^index/$', views.index),
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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
