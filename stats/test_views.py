from django.test import TestCase
from django.contrib.auth.models import User
from .models import BugWorkTime
from bugs.models import Post
from features.models import Feature


class TestFeatureList(TestCase):
    
    def test_stats_bugs_workflow_page(self):
        page = self.client.get("/stats/bugs/workflow")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "stats/workflow.html")
        
    def test_stats_bugs_by_upvotes_page(self):
        page = self.client.get("/stats/bugs/upvotes")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "stats/bugs_by_upvotes.html")
        
    def test_stats_for_features(self):
        page = self.client.get("/stats/features")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "stats/feature_stats.html")
        
        
class TestBugWorkTimeListApi(TestCase):
    
    def test_bug_work_time_daily(self):
        response = self.client.get("/stats/api/chart/data/daily")
        self.assertEqual(response.status_code, 200)
        
    def test_bug_work_time_weekly(self):
        response = self.client.get("/stats/api/chart/data/weekly")
        self.assertEqual(response.status_code, 200)
        
    def test_bug_work_time_monthly(self):
        response = self.client.get("/stats/api/chart/data/monthly")
        self.assertEqual(response.status_code, 200)
        
    def test_current_bug_upvotes(self):
        response = self.client.get("/stats/api/chart/data/bug/working/upvotes")
        self.assertEqual(response.status_code, 200)
        
    def test_open_bug_upvotes(self):
        response = self.client.get("/stats/api/chart/data/bug/open/upvotes")
        self.assertEqual(response.status_code, 200)
        
    def test_open_features_contributions(self):
        response = self.client.get("/stats/api/chart/data/feature/open/contributions")
        self.assertEqual(response.status_code, 200)
        
    def test_admin_panel_render_change_form(self):
        user = User.objects.create_superuser('superuser', 'myemail@test.com', password='password')
        post = Post(title="Test Feature", author=user, content="Test Content")
        post.save()
        data = {"bug": post, "user":user, "time_spent_mins":60, "timestamp":"2018-08-27"}
        self.client.login(username=user.username, password='password')
        response = self.client.post("/admin/stats/bugworktime/add/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        
    
