from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^create$', BlogCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[\d]+)$', BlogDetailView.as_view(), name='detail'),
    url(r'^(?P<blog_pk>[\d]+)/post/(?P<pk>[\d]+)$', PostDetailView.as_view(), name='post-detail'),
    url(r'^(?P<blog_pk>[\d]+)/create$', PostCreateView.as_view(), name='post-create'),
]
