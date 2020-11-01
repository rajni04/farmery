from django.contrib import admin
from post.models import Author, Post

admin.site.register(Author)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)