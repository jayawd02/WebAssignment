# Generated by Django 3.1.1 on 2020-10-27 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_auto_20200913_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='posted_by',
        ),
    ]
