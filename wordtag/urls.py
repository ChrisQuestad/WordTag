from django.conf.urls import url, include
from django.contrib import admin

from blogs.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
]