from django.test import TestCase
from models import Comment

class CommentTestCase(TestCase):
    def setUp(self):
        Comment.objects.create(name='Bob',email='123@qq.com',url='http://123.com',text='1111')


    def test_comment_name(self):
        Bob = Comment.objects.get(name='Bob')


