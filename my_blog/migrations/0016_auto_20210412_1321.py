# Generated by Django 3.1.7 on 2021-04-12 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0015_auto_20210412_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kelompok',
            name='jumlah',
        ),
        migrations.RemoveField(
            model_name='post',
            name='kategori2',
        ),
        migrations.AlterField(
            model_name='post',
            name='kategori',
            field=models.ForeignKey(choices=[('Sastra', 'Sastra'), ('Filsafat', 'Filsafat'), ('Politik', 'Politik'), ('Sejarah', 'Sejarah'), ('Opini', 'Opini'), ('hjksdk', 'hjksdk')], null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.kelompok'),
        ),
    ]
