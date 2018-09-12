from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, contribution_amount, empty_cart, remove_feature

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)$', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)$', adjust_cart, name='adjust_cart'),
    url(r'^empty-cart$', empty_cart, name='empty_cart'),
    url(r'^remove/(?P<id>\d+)$', remove_feature, name='remove_feature'),
    url(r'contribute/(?P<id>\d+)$', contribution_amount, name='contribution_amount'),
    ]