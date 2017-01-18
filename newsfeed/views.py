from django.shortcuts import render

from models import Hipster, Collection, Post  # noqa


def home_view(request):
    '''Display all public posts.'''
    posts = Post.objects.get_public_posts()
    context = {'posts': posts}

    return render(request, 'home.html', context)


def profile_view(request, profile):
    pass


def collection_view(request, profile, slug):
    pass
