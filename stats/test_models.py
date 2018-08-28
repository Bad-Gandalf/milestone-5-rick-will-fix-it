from django.test import TestCase
from .models import BugWorkTime
from django.contrib.auth.models import User
from bugs.models import Post
from datetime import datetime

# Create your tests here.
class TestBugWorkModel(TestCase):
    
    def test_str_is_equal_to_model_output(self):
        user = User.objects.create_user(username='username', password='password', is_staff=True)
        bug = Post(title="Test Bug", author=user, content="Test Content")
        bug.save()
        timesheet = BugWorkTime(bug=bug, user=user, timestamp="2018-08-28", time_spent_mins=60)
        self.assertEqual(timesheet.__unicode__(), 'Test Bug 60 2018-08-28 username')
        
        # self.bug.title, str(self.time_spent_mins), self.timestamp, self.user
        
    def test_bug_title_is_equal_to_model_output(self):
        user = User.objects.create_user(username='username', password='password', is_staff=True)
        bug = Post(title="Test Bug", author=user, content="Test Content")
        bug.save()
        timesheet = BugWorkTime(bug=bug, user=user, timestamp="2018-08-28", time_spent_mins=60)
        self.assertEqual(timesheet.bug_title, 'Test Bug')