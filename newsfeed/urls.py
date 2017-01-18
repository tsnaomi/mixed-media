from django.conf.urls import url

from views import (
    collection_view,
    home_view,
    profile_view,
    )

urlpatterns = [
    url(
        r'^$',
        home_view,
        name='home'),
    url(
        r'^(?P<profile>[-\w\d]+)$',
        profile_view,
        name='profile'),
    url(
        r'^(?P<profile>[-\w\d]+)/(?P<slug>[-\w%]+)$',
        collection_view,
        name='collection'),
    ]
