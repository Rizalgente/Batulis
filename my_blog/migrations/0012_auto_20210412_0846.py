# Generated by Django 3.1.7 on 2021-04-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0011_auto_20210412_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kategori2',
            field=models.CharField(choices=[('sosial-politik', 'Sosial-Politik'), ('filsafat', 'Filsafat'), ('sejarah', 'Sejarah'), ('none', 'None'), ('opini', 'Opini'), ('sastra', 'Sastra')], default='none', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=250), max_length=250),
        ),
    ]
