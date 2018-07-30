from django.conf.urls import url
from .views import post_detail, post_create, post_list, upvote_post

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
    url(r'^post_create/$', post_create, name="post_create"),
    url(r'^post_list/', post_list, name="post_list"),
    url(r'^upvote_post/$', upvote_post, name="upvote_post" ),
]