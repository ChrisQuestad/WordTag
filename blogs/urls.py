from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^create$', BlogCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)$', BlogDetailView.as_view(), name='detail'),
    url(r'^(?P<blog_pk>[\w-]+)/post/(?P<pk>[\w-]+)$', PostDetailView.as_view(), name='post-detail'),
    url(r'^(?P<blog_pk>[\w-]+)/create$', PostCreateView.as_view(), name='post-create'),
]
