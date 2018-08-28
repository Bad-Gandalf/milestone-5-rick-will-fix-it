from django.test import TestCase
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login
from .forms import CommentForm
# Create your tests here.
class TestPostList(TestCase):
    
    def test_post_list_retrieval_no_posts(self):
        page = self.client.get("/bugs/post_list/")
        self.assertQuerysetEqual(page.context["posts"], [])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_list.html")
    
    def test_post_list_retrieval(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
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
        
    
    def test_create_comment(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/{}/{}/".format(post.id, post.slug), {'content':'test comment',}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        self.assertContains(page, 'test comment')
        
        
    def test_create_comment_reply(self):   
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        comment1 = Comment(post=post, content="Comment 1", user=user)
        comment1.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/{}/{}/".format(post.id, post.slug), {'content':'test reply', 
                                                                            'reply': comment1}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        self.assertContains(page, 'Comment 1')
        self.assertContains(page, 'test reply')
        
    
        
    def test_upvote_post(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/upvote_post/", {'post_id' : post.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        self.assertTrue(page.context['is_upvoted'])
        
    def test_downvote_post(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        post.upvotes.add(user)
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/upvote_post/", {'post_id' : post.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        self.assertFalse(page.context['is_upvoted'])
    
    def test_like_comment(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        comment = Comment(post=post, content="Comment 1", user=user)
        comment.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/like_comment/", {'comment_id' : comment.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        
    def test_remove_like_comment(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        comment = Comment(post=post, content="Comment 1", user=user)
        comment.save()
        comment.likes.add(user)
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/like_comment/", {'comment_id' : comment.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        
    def test_update_post_get_page(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        self.client.login(username='username', password='password')
        page = self.client.get("/bugs/{0}/{1}/edit/".format(post.id, post.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_create.html")
        self.assertContains(page, "Test Content")
    
    def test_update_post(self):
        user = User.objects.create_user(username='username', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/bugs/{0}/{1}/edit/".format(post.id, post.slug), {"title": "Updated Post",
                                                                                    "content": "Updated Content"
        }, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/post_detail.html")
        self.assertContains(page, "Updated Content")
        
class TestAdminView(TestCase):
    def test_admin_queryset(self):
        user = User.objects.create_superuser('superuser', 'myemail@test.com', password='password')
        post = Post(title="Test Post", author=user, content="Test Content")
        post.save()
        self.client.login(username=user.username, password='password')
        
        response = self.client.get("/admin/bugs/post/")
        self.assertEqual(response.status_code, 200)   
        
   