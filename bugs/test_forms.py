from django.test import TestCase
from .forms import *

class TestCreatePostForm(TestCase):
    def test_create_post_with_just_title(self):
        form = PostCreateForm({'title':'TEST'})
        self.assertFalse(form.is_valid())
        
    def test_create_post_with_no_title(self):
        form = PostCreateForm({'content':'TEST-CONTENT'})
        self.assertFalse(form.is_valid())
        
    def test_create_post_with_no_image(self):
        form = PostCreateForm({'title':'TEST','content':'TEST-CONTENT'})
        self.assertTrue(form.is_valid())
    
class TestCreateCommentForm(TestCase):
    def test_create_comment_with_content(self):
        form = CommentForm({'content':'Test Content'})
        self.assertTrue(form.is_valid())
        
    def test_create_comment_without_content(self):
        form = CommentForm({'content':''})
        self.assertFalse(form.is_valid())
    