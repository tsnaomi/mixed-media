import re

from django.contrib.auth.models import User as AbstractUser
from django.db import models


# TODO: add managers, set up unique fields, default query orders

class Hipster(AbstractUser):
    pass


class Collection(models.Model):
    hipster = models.ForeignKey(Hipster)
    title = models.CharField(max_length=100, default='Untitled')
    title_slug = models.SlugField()
    is_public = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # on save, populate title_slut with a normalized version of title
        self.title_slug = '-'.join(re.split(r'[^A-Z0-9]+', self.title.lower()))

        super(Collection, self).save(*args, **kwargs)


class Post(models.Model):
    hipster = models.ForeignKey(Hipster)
    caption = models.CharField(max_length=100, default='Untitled')
    collection = models.ForeignKey(Collection)
    api = models.BooleanField()     # the API of the post (e.g., 'SoundCloud')
    source = models.URLField()      # the URL of the API resource
    date = models.DateTimeField(auto_now_add=True)
