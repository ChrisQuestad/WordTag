from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.AccountLoginView.as_view(), name='login'),
    url(r'^logout/$', views.AccountLogoutView.as_view(), name='logout'),
    url(r'^register/$', views.AccountRegisterView.as_view(), name='register'),
    url(r'^profile/$', views.AccountProfileView.as_view(), name='profile'),
]
