# Generated by Django 3.1.1 on 2020-09-13 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_postdislike_postlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='body',
            new_name='comment',
        ),
    ]
