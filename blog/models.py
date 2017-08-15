#!usr/bin/env python
# coding:utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('分类名称',max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField('标签名称',max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('标题',max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('发表时间')
    modified_time = models.DateTimeField('更新时间')
    excerpt = models.CharField('摘要',max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField('阅读',default=0)

    def __str__(self):
        return self.title
    #通过复写模型的 save 方法，从正文字段摘取前 N 个字符保存到摘要字段
    def save(self,*args,**kwargs):
        #如果没有摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

            # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time']


