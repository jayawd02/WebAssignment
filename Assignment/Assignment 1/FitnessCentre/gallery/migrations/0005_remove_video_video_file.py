# Generated by Django 3.1.1 on 2020-09-04 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_recipeimage_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
    ]