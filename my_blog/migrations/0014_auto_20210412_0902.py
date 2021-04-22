# Generated by Django 3.1.7 on 2021-04-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0013_auto_20210412_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kategori2',
            field=models.CharField(choices=[('sosial-politik', 'Sosial-Politik'), ('sastra', 'Sastra'), ('filsafat', 'Filsafat'), ('sejarah', 'Sejarah'), ('opini', 'Opini'), ('none', 'None')], default='none', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='jj'),
        ),
    ]
