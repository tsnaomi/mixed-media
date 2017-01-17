from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager

# TODO: add default ordering


class HipsterManager(BaseUserManager):

    def add_user(self, username, email, password):
        '''Add the hipster to the database.'''
        hipster = self.Model(username=username.lower(), email=email.lower())
        hipster.set_password(password)
        hipster.save(using=self._db)

        return hipster


class CollectionManager(Manager):

    def get_public_collections(self, user):
        '''Return all of the public collections for a given user.'''
        return self.filter(hipster=user, is_public=True)

    def get_all_collections(self, user):
        '''Return all of the collections for a given user.'''
        return self.filter(hipster=user)

    def get_collection(self, user, title_slug):
        '''Return the specified collection for a given user.'''
        return self.filter(hipster=user, title_slug=title_slug)


class PostManager(Manager):

    def get_public_posts(self):
        '''Return all of the public posts.'''
        return self.filter(collection__public=True)

    def get_user_posts(self, user):
        '''Return all of the posts for a given user.'''
        return self.filter(hipster=user)

    def get_user_public_posts(self, user):
        '''Return all of the public posts for a given user.'''
        return self.filter(hipster=user, collection__public=True)
