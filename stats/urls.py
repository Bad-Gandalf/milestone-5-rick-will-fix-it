from django.conf.urls import url
from .views import BugWorkTimeListDaily, display_stats, BugWorkTimeListWeekly, BugWorkTimeListMonthly, CurrentBugUpvotes
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/chart/data/daily', BugWorkTimeListDaily.as_view(), name="workflow_daily"),
    url(r'^api/chart/data/weekly', BugWorkTimeListWeekly.as_view(), name="workflow_weekly"),
    url(r'^api/chart/data/monthly', BugWorkTimeListMonthly.as_view(), name="workflow_monthly"),
    url(r'^api/chart/data/bug/upvotes', CurrentBugUpvotes.as_view(), name="current_bugs_upvotes"),
    
    url(r'^$', display_stats, name="workflow"),
    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)