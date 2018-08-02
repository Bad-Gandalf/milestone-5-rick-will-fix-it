from django.conf.urls import url
from .views import post_detail, post_create, post_list, upvote_post, like_comment, post_update

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
    url(r'^post_create/$', post_create, name="post_create"),
    url(r'^post_list/', post_list, name="post_list"),
    url(r'^upvote_post/$', upvote_post, name="upvote_post"),
    url(r'^like_comment/$', like_comment, name="like_comment"),
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
]