from django.contrib.auth.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name = 'post_share'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]