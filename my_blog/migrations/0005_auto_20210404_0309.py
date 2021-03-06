# Generated by Django 3.1.7 on 2021-04-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_auto_20210331_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelompok',
            name='jumlah',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publised', 'Publised')], default='draft', max_length=9),
        ),
    ]
