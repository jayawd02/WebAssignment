# Generated by Django 3.1.1 on 2020-09-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6),
        ),
    ]