from django.contrib import admin
from my_blog.models import Post, Penulis, Kelompok

class Project(admin.ModelAdmin):
    post = Post
    list_display = ('id', 'title', 'author', 'kategori', 'publised', 'created','update', 'status',)
    list_display_links = ('id', 'title')
    list_per_page = 8

admin.site.register(Post, Project)
admin.site.register(Penulis)
admin.site.register(Kelompok)
