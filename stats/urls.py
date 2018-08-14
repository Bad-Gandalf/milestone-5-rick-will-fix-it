from django.conf.urls import url
from .views import BugWorkTimeList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', BugWorkTimeList.as_view(), name="workflow"),
    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)