from django.test import TestCase
from .models import Feature, Comment
from checkout.models import Order, OrderLineItem
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login
from django.utils import timezone

class TestFeatureList(TestCase):
    
    def test_feature_list_retrieval_no_features(self):
        page = self.client.get("/features/feature_list/")
        self.assertQuerysetEqual(page.context["features"], [])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_list.html")
    
    def test_Feature_list_retrieval(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        page = self.client.get("/features/feature_list/")
        self.assertTrue(page.context["features"])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_list.html")
        
class TestFeatureDetailView(TestCase):
    
    def test_feature_detail(self):
        user = User(username="username", email="email@gmail.com", password="password")
        user.save()
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        page = self.client.get("/features/{0}/{1}/".format(feature.id, feature.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertContains(page, 'Test Feature')
        
    def test_create_feature_post(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.post("/features/feature_create/", { 
                                                        'content':'test content',
                                                        'title': 'test feature'}, 
                                                        follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertContains(page, 'test feature')
        
    def test_create_feature_get(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/features/feature_create/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_create.html")
        
    def test_create_comment(self):
        user = User.objects.create_user(username='username', password='password')
        feature = Feature(title="Test Post", author=user, content="Test Content")
        feature.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/features/{}/{}/".format(feature.id, feature.slug), {'content':'test comment',}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertContains(page, 'test comment')
        
    def test_create_reply_to_comment_with_existing_replies(self):
        user = User.objects.create_user(username='username', password='password')
        feature = Feature(title="Test Post", author=user, content="Test Content")
        feature.save()
        comment1 = Comment(feature=feature, content="Comment 1", user=user)
        comment1.save()
        reply1 = Comment(feature=feature, content="Reply 1", user=user, reply=comment1)
        reply1.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/features/{}/{}/".format(feature.id, feature.slug), {'content':'test reply 2',
                                                                    'reply_id': comment1.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertContains(page, 'Comment 1')
        self.assertContains(page, 'Reply 1')
        self.assertContains(page, 'test reply 2')
        
    def test_like_comment(self):
        user = User.objects.create_user(username='username', password='password')
        feature = Feature(title="Test Post", author=user, content="Test Content")
        feature.save()
        comment = Comment(feature=feature, content="Comment 1", user=user)
        comment.save()
        self.client.login(username='username', password='password')
        page = self.client.post("/features/like_comment/", {'comment_id' : comment.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertContains(page, 'Comment 1')
        self.assertEqual(comment.total_likes(), 1)
        
    def test_remove_like_comment(self):
        user = User.objects.create_user(username='username', password='password')
        feature = Feature(title="Test Post", author=user, content="Test Content")
        feature.save()
        comment = Comment(feature=feature, content="Comment 1", user=user)
        comment.save()
        comment.likes.add(user)
        self.client.login(username='username', password='password')
        page = self.client.post("/features/like_comment/", {'comment_id' : comment.id}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertContains(page, 'Comment 1')
        self.assertEqual(comment.total_likes(), 0)
        
        
    def test_total_contributions(self):
        user = User.objects.create_user(username='username', password='password')
        feature = Feature(title="Test Post", author=user, content="Test Content")
        feature.save()
        order = Order(full_name = "Patrick Doherty",
                    phone_number = "02871774646",
                    country = "Ireland",
                    postcode = "BT829DE",
                    town_or_city = "Strabane",
                    street_address1 = "5 Lasts Lane",
                    street_address2 = "Urney Road",
                    county = "Tyrone",
                    date = timezone.now())
        order.save()
        contribution = OrderLineItem(order=order, feature=feature, user=user, contribution =50)
        contribution.save()
        page = self.client.get("/features/{0}/{1}/".format(feature.id, feature.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature_detail.html")
        self.assertEqual(page.context["total_contributions"], 50)
        self.assertContains(page, 'Test Content')
        self.assertEqual(str(order), "{0}-{1}-{2}".format(order.id, order.date, order.full_name))
        self.assertEqual(str(contribution), "{0}-{1}-{2}".format(contribution.contribution, feature.title, user.username))
        
        
            