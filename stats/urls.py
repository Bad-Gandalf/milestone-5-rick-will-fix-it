from django.conf.urls import url
from .views import bug_workflow

urlpatterns = [
    url(r'bug_workflow/', bug_workflow, name="bug_workflow"),
    
    
]