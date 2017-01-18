from django.shortcuts import render
from django.http import Http404

from models import Hipster, Collection, Post


# IMPLEMENT: sign-in, sign-out, search
# CONSIDER: implementing separate collection pages


def home_view(request):
    '''Display all public posts.'''
    posts = Post.objects.get_public_posts()
    context = {'posts': posts}

    return render(request, 'newsfeed.html', context)


def profile_view(request, profile):
    '''Display a hipster's profile.'''
    hipster = Hipster.objects.get(username=profile)

    if hipster:

        if hipster == request.user:
            is_owner = True
            collections = Collection.objects.get_all_collections(hipster)
            posts = Post.objects.get_user_posts(hipster)

        else:
            is_owner = False
            collections = Collection.objects.get_public_collections(hipster)
            posts = Post.objects.get_user_public_posts(hipster)

        context = {
            'is_owner': is_owner,
            'collections': collections,
            'posts': posts,
            }

        return render(request, 'newsfeed.html', context)

    raise Http404
