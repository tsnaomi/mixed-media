from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from models import Collection, Hipster, Post


# Inline Admins ---------------------------------------------------------------

class CollectionInlineAdmin(admin.TabularInline):
    model = Collection
    fieldsets = (
        (None,
            {'fields': (
                'title',
                'date',
                'is_public',
                )},),
        )
    readonly_fields = (
        'date',
        )


class PostInlineAdmin(admin.TabularInline):
    model = Post
    fieldsets = (
        (None,
            {'fields': (
                'caption',
                'api',
                'source',
                'date',
                )},),
        )
    readonly_fields = (
        'date',
        )


# Model Admins ----------------------------------------------------------------

class HipsterAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'is_admin',
        )
    fieldsets = (
        ('HIPSTER',
            {'fields': (
                'username',
                'email',
                'password',
                'is_admin',
                )},),
        )
    list_filter = (
        'is_admin',
        )
    filter_horizontal = ()
    inlines = (
        CollectionInlineAdmin,
        )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'hipster',
        'title',
        'is_public',
        'date',
        )
    fieldsets = (
        ('COLLECTION',
            {'fields': (
                'hipster',
                'title',
                'title_slug',
                'date',
                'is_public',
                )},),
        )
    list_filter = (
        'is_public',
        )
    readonly_fields = (
        'title_slug',
        'date',
        )
    inlines = (
        PostInlineAdmin,
        )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'hipster',
        'collection',
        'api',
        'caption',
        'source',
        'date',
        )
    fieldsets = (
        ('POST',
            {'fields': (
                'hipster',
                'collection',
                'caption',
                'api',
                'source',
                'date',
                )},),
        )
    search_fields = (
        'hipster__username',
        'collection__title',
        'api',
        'caption',
        'source',
        )
    readonly_fields = (
        'date',
        )


# Admin Registration ----------------------------------------------------------

admin.site.register(Hipster, HipsterAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Post, PostAdmin)

admin.site.unregister(Group)
