from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Penulis(models.Model):
    nama = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

class Kelompok(models.Model):
    kelompok = models.CharField(max_length=15)

    def __str__(self):
        return self.kelompok

class PostUser(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('publised', 'Publised'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='cover/', null=True)
    content = RichTextField(blank=True, null=True)
    content2 = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    seo_title = models.CharField(max_length=250, blank=True)
    seo_description = models.CharField(max_length=160, blank=True)
    author = models.ForeignKey(Penulis, related_name='blog_post', on_delete=models.CASCADE)
    publised = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    kategori = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    Genre = models.CharField(max_length=25, default='Buku', blank=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug', self.slug})
    

    def __str__(self):
        return self.title
    
       

