# Generated by Django 3.1.1 on 2020-09-13 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0011_auto_20200911_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='gallery.post')),
                ('users', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='gallery.post')),
                ('users', models.ManyToManyField(related_name='post_dislikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
