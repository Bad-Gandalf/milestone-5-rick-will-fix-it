from django.conf.urls import url
from .views import feature_list, feature_detail, feature_create, like_feature_comment

urlpatterns = [
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', feature_detail, name='feature_detail'),
    url(r'feature_create/$', feature_create, name="feature_create"),
    url(r'feature_list/', feature_list, name="feature_list"),
    url(r'^like_feature_comment/$', like_feature_comment, name="like_feature_comment"),
    
]