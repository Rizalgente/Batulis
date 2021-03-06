# Generated by Django 3.1.7 on 2021-04-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0012_auto_20210412_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kategori2',
            field=models.CharField(choices=[('none', 'None'), ('filsafat', 'Filsafat'), ('sosial-politik', 'Sosial-Politik'), ('sastra', 'Sastra'), ('sejarah', 'Sejarah'), ('opini', 'Opini')], default='none', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publised', 'Publised')], default='draft', max_length=9),
        ),
    ]
