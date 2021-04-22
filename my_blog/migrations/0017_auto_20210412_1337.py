# Generated by Django 3.1.7 on 2021-04-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0016_auto_20210412_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Genre',
        ),
        migrations.AlterField(
            model_name='post',
            name='kategori',
            field=models.ForeignKey(choices=[('Sastra', 'Sastra'), ('Filsafat', 'Filsafat'), ('Politik', 'Politik'), ('Sejarah', 'Sejarah'), ('Opini', 'Opini')], null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.kelompok'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('publised', 'Publised'), ('draft', 'Draft')], default='draft', max_length=9),
        ),
    ]
