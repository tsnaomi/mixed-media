from django.conf.urls import url

from views import (
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
    ]
