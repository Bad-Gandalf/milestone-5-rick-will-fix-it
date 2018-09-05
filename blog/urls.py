from django.conf.urls import url
from .views import blog_detail, index

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', blog_detail, name='blog_detail'),
    
    ]