# Generated by Django 3.1.7 on 2021-03-31 14:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jumbotron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=50)),
                ('judul2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='cover/')),
            ],
        ),
    ]
