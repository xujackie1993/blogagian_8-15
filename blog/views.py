#!/usr/bin/env python
# coding:utf-8

from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView
import logging
import MySQLdb as mdb

# def index(request):
#     post_list = Post.objects.all()
#     return render(request,'blog/index.html',context={
#         'post_list':post_list
#     })
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

def detail(request,pk):

    post = get_object_or_404(Post, pk=pk)
    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = { 'post':post,
                'form':form,
                'comment_list':comment_list
                }

    return render(request, 'blog/detail.html', context=context)

'''归档'''
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})

def tags(request,pk):
    tag = get_object_or_404(Tag,pk=pk)
    post_list = Post.objects.filter(tags=tag)
    return render(request,'blog/index.html',context={'post_list':post_list})

def about(request):
    return render(request,'blog/about.html',context={'welcome':'欢迎来到我的博客',
                                                     'myblog':'我的博客'})
def contact(request):
    return render(request,'blog/contact.html',context={'contactme':'联系我'})



logger = logging.getLogger('blog.views')
try:
    mysql= mdb.connect('127.0.0.1', '3306', 'david')
except Exception,e:
            logger.error(e)        #直接将错误写入到日志文件