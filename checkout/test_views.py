from django.test import TestCase
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from features.models import Feature
from .forms import *
from django.utils import timezone
from django.conf import settings

class TestCheckoutViews(TestCase):
    
    def test_checkout_with_correct_card_details(self):
        user = User.objects.create_user('username', 'myemail@test.com','password')
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        self.client.login(username='username', password='password')
        self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': '50'}, follow=True)
        stripe_id = 'tok_visa'
        
        page = self.client.post('/checkout/', {'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
        self.assertEqual(page.status_code, 200)
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertTemplateUsed('features/feature_detail.html')
        self.assertEqual(str(messages[0]), 'You have successfully contributed')
    
    def test_checkout_with_incorrect_card_details(self):
        user = User.objects.create_user('username', 'myemail@test.com','password')
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        
        self.client.login(username='username', password='password')
        self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': '50'}, follow=True)
        stripe_id = 'tok_chargeDeclined'
        page = self.client.post('/checkout/', {'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4000400040004000','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id} , follow=True)
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'Your card was declined!')
        
    def test_checkout_invalid_order_form(self):
        user = User.objects.create_user('username', 'myemail@test.com','password')
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        
        self.client.login(username='username', password='password')
        self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': '50'}, follow=True)
        stripe_id = 'tok_chargeDeclined'
        page = self.client.post('/checkout/', {'phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4000400040004000','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id} , follow=True)
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'We were unable to take a payment with that card!')
        
    def test_load_page(self):
        user = User.objects.create_user('username', 'myemail@test.com','password')
        feature = Feature(title="Test Feature", author=user, content="Test Content")
        feature.save()
        self.client.login(username='username', password='password')
        self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': '50'}, follow=True)
        stripe_id = 'tok_visa'
        page=self.client.get('/checkout/')
        self.assertTemplateUsed('checkout/checkout.html')
        