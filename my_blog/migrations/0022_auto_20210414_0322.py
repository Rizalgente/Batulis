# Generated by Django 3.1.7 on 2021-04-14 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0021_auto_20210414_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publised', 'Publised')], default='draft', max_length=9),
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='tags'),
        ),
    ]