# Generated by Django 3.1.7 on 2021-04-12 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0017_auto_20210412_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Genre',
            field=models.CharField(default='Buku', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.kelompok'),
        ),
    ]
