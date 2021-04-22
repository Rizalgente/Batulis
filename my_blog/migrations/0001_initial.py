# Generated by Django 3.1.7 on 2021-03-30 19:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelompok', models.CharField(max_length=15)),
                ('jumlah', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Penulis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('image', models.ImageField(null=True, upload_to='cover/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content2', models.TextField(blank=True)),
                ('seo_title', models.CharField(blank=True, max_length=250)),
                ('seo_description', models.CharField(blank=True, max_length=160)),
                ('publised', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('publised', 'Publised'), ('draft', 'Draft')], default='draft', max_length=9)),
                ('Genre', models.CharField(default='Book', max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to='my_blog.penulis')),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.kelompok')),
            ],
        ),
    ]