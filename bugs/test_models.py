from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment, Post

class TestCommentModel(TestCase):
    
    def test_str_is_equal_to_username(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        comment = Comment(content="Test Comment", post=post, user=user)
        self.assertEqual(str(comment), 'Test Post-username')