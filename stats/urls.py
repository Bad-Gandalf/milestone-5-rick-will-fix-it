from django.conf.urls import url
from .views import BugWorkTimeList, display_stats
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/chart/data', BugWorkTimeList.as_view(), name="workflow"),
    url(r'^$', display_stats, name="workflow"),
    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)