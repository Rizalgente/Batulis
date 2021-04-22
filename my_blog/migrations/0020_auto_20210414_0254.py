# Generated by Django 3.1.7 on 2021-04-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0019_auto_20210412_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publised', 'Publised')], default='draft', max_length=9),
        ),
    ]