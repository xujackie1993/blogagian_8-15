#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Xuzhenjie on 2017/7/28
'''
我们的博客侧边栏有四项内容：最新文章、归档、分类和标签云，使用自定义模板标签  先写好函数，然后将函数注册为模板标签
'''
from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

'''
 dates 方法会返回一个列表,列表中的元素为每一篇文章（Post）的创建时间，且是 Python 的 date 对象，精确到月份，降序排列
'''
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类   gt 是 django 的查询表达式 表示大于
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

