#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Xuzhenjie on 2017/7/28
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','text']
