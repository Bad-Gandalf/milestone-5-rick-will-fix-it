from django.test import TestCase
from features.models import Feature
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login

class TestCartViews(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='username', password='password')
        self.feature = Feature(title="Test Feature", author=self.user, content="Test Content")
        self.feature.save()
       
    def test_empty_cart_view(self):
        self.client.login(username='username', password='password')
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html')
        
    def test_contribution_amount(self):
        self.client.login(username='username', password='password')
        page = self.client.get('/cart/contribute/{0}'.format(self.feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/contribution_amount.html')
        
    def test_add_to_cart(self):
        self.client.login(username='username', password='password')
        page = self.client.post('/cart/add/{0}'.format(self.feature.id), {'contribution': '50'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html')
        
    def test_adjust_cart_minimum_amount_10_euro(self):
        self.client.login(username='username', password='password')
        page = self.client.post('/cart/adjust/{0}'.format(self.feature.id), {'contribution': '10'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html')
        
    def test_adjust_cart_below_minimum_amount_10_euro(self):
        self.client.login(username='username', password='password')
        page = self.client.post('/cart/adjust/{0}'.format(self.feature.id), {'contribution': '9'}, follow=True)
        messages = list(page.context['messages'])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html')
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Contributions must be at least €10')
        
    def test_adjust_cart_0_euro_or_empty(self):
        self.client.login(username='username', password='password')
        page = self.client.post('/cart/adjust/{0}'.format(self.feature.id), {'contribution': '0'}, follow=True)
        messages = list(page.context['messages'])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html')
        
    def test_empty_cart(self):
        self.client.login(username='username', password='password')
        page = self.client.post('/cart/add/{0}'.format(self.feature.id), {'contribution': '50'}, follow=True)
        page = self.client.post('/cart/empty-cart', follow=True)
        messages = list(page.context['messages'])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html') 
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have successfully emptied your cart!')
        
    def test_remove_feature_from_cart(self):
        self.client.login(username='username', password='password')
        page = self.client.post('/cart/add/{0}'.format(self.feature.id), {'contribution': '50'}, follow=True)
        page = self.client.post('/cart/remove/{0}'.format(self.feature.id), follow=True)
        messages = list(page.context['messages'])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html') 
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Feature successfully deleted from cart!')
        