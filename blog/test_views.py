from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User
from django.utils import timezone

class TestBlogViews(TestCase):
    
    def test_blog_list_retrival_with_blog(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        blog = Blog(author=user, title="Test Title", content="Test Content", published_date=timezone.now())
        blog.save()
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/index.html")
        self.assertTrue(page.context["blogs"])

    def test_blog_list_retrival_without_blog(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/index.html")
        self.assertFalse(page.context["blogs"])
        
    def test_blog_detail_view(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        blog = Blog(author=user, title="Test Title", content="Test Content", published_date=timezone.now())
        blog.save()
        page = self.client.get("/blog/{}/{}/".format(blog.id, blog.slug), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/blog_detail.html")
        self.assertTrue(page.context["blog"])
        
    def test_admin_panel_render_change_form(self):
        user = User.objects.create_superuser('superuser', 'myemail@test.com', password='password')
        data = {"title": "test Title", "author":user, "content":'test content', 'published_date':timezone.now()}
        self.client.login(username=user.username, password='password')
        response = self.client.post("/admin/blog/blog/add/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        