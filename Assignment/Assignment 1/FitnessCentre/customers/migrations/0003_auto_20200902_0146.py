# Generated by Django 3.1 on 2020-09-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200902_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membershipplan',
            old_name='duration',
            new_name='duration (months)',
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10),
        ),
    ]
