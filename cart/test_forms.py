from django.test import TestCase
from .forms import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from features.models import Feature

class TestContributionForm(TestCase):
    
    def test_form_with_less_that_10_euro(self):
        form = ContributionForm({'contribution':9})
        self.assertTrue(form.is_valid())
        self.assertRaises(ValidationError, form.clean_price)
        
    
        
        
        
