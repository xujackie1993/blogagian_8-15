#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Xuzhenjie on 2017/7/27
'''
create some records for demo databases
'''

from blogagain.wsgi import *
from blog.models import Category,Tag,Post

def main():
    category_tag = [
        ('blog','python'),
        ('article', 'django'),
        ('record', 'django'),
    ]
    for category, tag in category_tag:
        c = Category.objects.get_or_create(name=category)[0]
        t = Tag.objects.get_or_create(name=tag)[0]
        #创建10篇新闻
        for i in range(1,11):
            post = Post.objects.get_or_create(
                title = '{}_{}'.format(category,i),
                body = '详细内容： {} {}'.format(tag, i)
            )[0]
            post.category.add(c)
            post.tags.add(t)

if __name__=='__main__':
    main()
    print 'Done!'
