from django.test import TestCase
from django.contrib.auth import login
from django.contrib.auth.models import User
from features.models import Feature
from .forms import *
from django.utils import timezone
from django.conf import settings
import env
import stripe

stripe.api_key = settings.STRIPE_SECRET



# class TestCheckoutViews(TestCase):
#     def test_checkout_with_incorrect_card_details(self):
#         user = User.objects.create_user(username='username', password='password')
#         feature = Feature(title="Test Feature", author=user, content="Test Content")
#         feature.save()
#         self.client.login(username='username', password='password')
#         self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': '50'}, follow=True)
#         token = stripe.Token.create(
#             card={
#                 "number": '4242424242424242',
#                 "exp_month": 12,
#                 "exp_year": 2019,
#                 "cvc": '111'
#                 },
#                 )
        
        
#         page = self.client.post('/checkout/', {'full_name':"Patrick Doherty",
#                 'phone_number':"02871774646",
#                 'country':"Ireland",
#                 'postcode':"BT829DE",
#                 'town_or_city':"Strabane",
#                 'street_address1':'5 Lasts Lane',
#                 'street_address2':"Urney Road",
#                 'county':"Tyrone",
#                 token
#             }, follow=True)
#         self.assertEqual(page.status_code, 200)
#         messages = list(page.context['messages'])
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'We were unable to take a payment with that card!')
    
#     def test_checkout_with_correct_card_details(self):
#         user = User.objects.create_user(username='username', password='password')
#         feature = Feature(title="Test Feature", author=user, content="Test Content")
#         feature.save()
        
#         self.client.login(username='username', password='password')
#         self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': '50'}, follow=True)
#         page = self.client.post('/checkout/', {'full_name':"Patrick Doherty",
#                 'phone_number':"02871774646",
#                 'country':"Ireland",
#                 'postcode':"BT829DE",
#                 'town_or_city':"Strabane",
#                 'street_address1':'5 Lasts Lane',
#                 'street_address2':"Urney Road",
#                 'county':"Tyrone",
#                 'credit_card_number':'42424242424243',
#                 'cvv':'111',
#                 'expiry_month': '12',
#                 'expiry_year':'2019',
#                 'stripe_id': settings.STRIPE_PUBLISHABLE} , follow=True)
#         self.assertEqual(page.status_code, 200)
#         messages = list(page.context['messages'])
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'We were unable to take a payment with that card!')