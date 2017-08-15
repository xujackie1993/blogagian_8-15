#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Xuzhenjie on 2017/7/28

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tags/(?P<pk>[0-9]+)/$',views.tags,name='tags'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact')
]
