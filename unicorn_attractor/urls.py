from django.conf.urls import url, include
from django.contrib import admin
from blog.views import index
from accounts import urls as accounts_urls
from bugs import urls as bugs_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from features import urls as features_urls
from stats import urls as stats_urls
from blog import urls as blog_urls
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^bugs/', include(bugs_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^features/', include(features_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^stats/', include(stats_urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    
    
]
