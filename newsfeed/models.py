import re

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from managers import CollectionManager, HipsterManager, PostManager


class Hipster(AbstractBaseUser):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField(unique=True, default=None)
    is_admin = models.BooleanField(default=False)

    objects = HipsterManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        ordering = ['username', ]

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.is_admin

    def is_active(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label=None):
        return self.is_admin

    def get_short_name(self):
        return self.username


class Collection(models.Model):
    hipster = models.ForeignKey(Hipster)
    title = models.CharField(max_length=40, default='Untitled')
    title_slug = models.SlugField(blank=True)
    is_public = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    objects = CollectionManager()

    class Meta:
        unique_together = ('hipster', 'title_slug')
        ordering = ['-date', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # on save, populate title_slug with a normalized version of title
        self.title_slug = '-'.join(re.split(r'[^a-z0-9]+', self.title.lower()))

        super(Collection, self).save(*args, **kwargs)


class Post(models.Model):
    SOUNDCLOUD = 'SC'
    FLICKR = 'FL'
    YOUTUBE = 'YT'

    APIs = (
        (SOUNDCLOUD, 'SoundCloud'),
        (FLICKR, 'Flickr'),
        (YOUTUBE, 'Youtube'),
        )

    hipster = models.ForeignKey(Hipster, blank=True)
    caption = models.CharField(max_length=100, default='Untitled')
    collection = models.ForeignKey(Collection)
    api = models.CharField(max_length=2, choices=APIs)  # the API of the post
    source = models.URLField()  # the URL of the API resource
    # is_starred = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return '%s (@%s)' % (self.caption, self.hipster.username)

    def save(self, *args, **kwargs):
        # on save, populate hipster with the collection's hipster
        self.hipster = self.collection.hipster

        super(Post, self).save(*args, **kwargs)
