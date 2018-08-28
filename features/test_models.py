from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment, Feature

class TestCommentModel(TestCase):
    
    def test_str_is_equal_to_username(self):
        user = User.objects.create_user(username='username', password='password')
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        comment = Comment(content="Test Comment", feature=feature, user=user)
        self.assertEqual(str(comment), 'Test Feature-username')