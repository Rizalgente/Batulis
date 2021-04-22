from django.contrib import admin
from projectUser.models import PostUser, Kelompok, Penulis

class Project(admin.ModelAdmin):
    post = PostUser
    list_display = ('id', 'title', 'author', 'kategori', 'publised', 'created','update', 'status',)
    list_display_links = ('id', 'title')
    list_per_page = 8

admin.site.register(PostUser, Project)
admin.site.register(Kelompok)
admin.site.register(Penulis)