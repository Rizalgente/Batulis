# Generated by Django 3.1.7 on 2021-04-04 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0007_auto_20210404_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kategori2',
            field=models.CharField(choices=[('sosial-politik', 'Sosial-Politik'), ('sastra', 'Sastra'), ('sejarah', 'Sejarah'), ('none', 'None'), ('filsafat', 'Filsafat')], default='None', max_length=15),
        ),
    ]
