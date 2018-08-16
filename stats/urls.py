from django.conf.urls import url
from .views import (BugWorkTimeListDaily, display_stats, BugWorkTimeListWeekly, \
BugWorkTimeListMonthly, CurrentBugUpvotes, OpenBugUpvotes, OpenFeaturesContributions, \
display_feature_stats)

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/chart/data/daily', BugWorkTimeListDaily.as_view(), name="workflow_daily"),
    url(r'^api/chart/data/weekly', BugWorkTimeListWeekly.as_view(), name="workflow_weekly"),
    url(r'^api/chart/data/monthly', BugWorkTimeListMonthly.as_view(), name="workflow_monthly"),
    url(r'^api/chart/data/bug/working/upvotes', CurrentBugUpvotes.as_view(), name="current_bugs_upvotes"),
    url(r'^api/chart/data/bug/open/upvotes', OpenBugUpvotes.as_view(), name="open_bugs_upvotes"),
    url(r'^api/chart/data/feature/open/contributions', OpenFeaturesContributions.as_view(), name="open_feature_contributions"),
    
    url(r'^bugs$', display_stats, name="workflow"),
    url(r'^features$', display_feature_stats, name="feature_contributions")
    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)