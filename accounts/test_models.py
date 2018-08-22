from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.
class TestProfileModel(TestCase):
    def test_default_profile_settings(self):
        user = User.objects.create_user(username='username', password='password')
        user.save()
        profile = get_object_or_404(Profile, user=user.id)
        self.assertEqual(profile.photo, "img/blank_avatar.png")
        self.assertFalse(profile.date_of_birth)
        self.assertFalse(profile.location)
        self.assertFalse(profile.bio)
        
    def test_str_is_equal_to_username(self):
        user = User.objects.create_user(username='username', password='password')
        user.save()
        profile = get_object_or_404(Profile, user=user.id)
        self.assertEqual(str(profile), 'Profile for user username')