from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager


class HipsterManager(BaseUserManager):

    def create_user(self, username, email, password):
        '''Add a hipster to the database.'''
        hipster = self.model(username=username.lower(), email=email.lower())
        hipster.set_password(password)
        hipster.save(using=self._db)

        return hipster

    def create_superuser(self, username, email, password):
        '''Add super hipster to the database.'''
        hipster = self.create_user(
            username=username,
            email=email,
            password=password,
            )
        hipster.is_admin = True
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
        return self.filter(collection__is_public=True)

    def get_user_posts(self, user):
        '''Return all of the posts for a given user.'''
        return self.filter(hipster=user)

    def get_user_public_posts(self, user):
        '''Return all of the public posts for a given user.'''
        return self.filter(hipster=user, collection__is_public=True)
