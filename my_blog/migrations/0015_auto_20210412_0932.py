# Generated by Django 3.1.7 on 2021-04-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0014_auto_20210412_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kategori2',
            field=models.CharField(choices=[('sastra', 'Sastra'), ('sosial-politik', 'Sosial-Politik'), ('none', 'None'), ('filsafat', 'Filsafat'), ('opini', 'Opini'), ('sejarah', 'Sejarah')], default='none', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]
