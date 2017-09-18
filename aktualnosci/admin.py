from django.contrib import admin
from django.db import models
from .models import Post

from pagedown.widgets import AdminPagedownWidget

class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
         models.TextField: {'widget': AdminPagedownWidget },
    }

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created', 'status']
    list_filter = ['publish', 'status', 'author']
    search_fields = ['title', 'body']

admin.site.register(Post, PostAdmin)
