# Generated by Django 3.1.1 on 2020-09-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20200906_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
