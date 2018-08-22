from django.test import TestCase
from .forms import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 

# Create your tests here.
class TestRegistrationForm(TestCase):
    
    def test_can_create_account_with_just_a_username(self):
        form = UserRegistrationForm({'username': 'test_username'})
        self.assertFalse(form.is_valid()) #Passes
        
    def test_correct_message_for_missing_username(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_correct_message_for_missing_email_address(self):
        form = UserRegistrationForm({'username': 'test_username', 
                                        'email': '',
                                        'password1': 'beyk38cmej39',
                                        'password2': 'beyk38cmej39'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])
        
    def test_correct_message_for_missing_password1(self):
        form = UserRegistrationForm({'username': 'test_username', 
                                        'email': 'email.address@gmail.com',
                                        'password1': '',
                                        'password2': 'beyk38cmej39'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
        self.assertRaises(ValidationError, form.clean_password)
        
    def test_correct_message_for_missing_password2(self):
        form = UserRegistrationForm({'username': 'test_username', 
                                        'email': 'email.address@gmail.com',
                                        'password1': 'beyk38cmej39',
                                        'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
        self.assertRaises(ValidationError, form.clean_password)
        
    def test_correct_form_inputs(self):
        form = UserRegistrationForm({'username': 'test_username', 
                                        'email': 'email.address@gmail.com',
                                        'password1': 'beyk38cmej39',
                                        'password2': 'beyk38cmej39'})
        self.assertTrue(form.is_valid())  
        
    def test_password_match_message(self):
        form = UserRegistrationForm({'username': 'test_username', 
                                        'email': 'email.address@gmail.com',
                                        'password1': 'beyk38cmej39',
                                        'password2': 'Xeyk38cmej39'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u"The two password fields didn't match."])
        self.assertRaises(ValidationError, form.clean_password)
        
        
    def test_email_address_is_unique_true(self):
        User.objects.create_user(username='test_username', password='password', email='email.address@gmail.com')
        
        form = UserRegistrationForm({'username': 'test_username1', 
                                        'email': 'email.address@gmail.com',
                                        'password1': 'Xeyk38cmej39',
                                        'password2': 'Xeyk38cmej39'})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'Email address must be unique'])
        
       