from django.test import TestCase
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login
from .forms import CommentForm
# Create your tests here.
class TestPostList(TestCase):
    def setUp(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
    
    def test_post_list_retrieval(self):
        page = self.client.get("/bugs/post_list/")
        self.assertTrue(page.context["posts"])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_list.html")

class TestPostDetailView(TestCase):
    
    def test_post_detail(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        page = self.client.get("/bugs/{0}/{1}/".format(post.id, post.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
    
    def test_create_post_post(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/post_create/", {'author': user, 'content':'test content', 'title': 'test title'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        
    def test_create_post_get(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/bugs/post_create/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_create.html")
        
    