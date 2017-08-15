#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Xuzhenjie on 2017/7/28
from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]