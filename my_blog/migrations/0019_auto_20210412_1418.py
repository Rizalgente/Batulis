# Generated by Django 3.1.7 on 2021-04-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0018_auto_20210412_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Genre',
            field=models.CharField(blank=True, default='Buku', max_length=25),
        ),
    ]
