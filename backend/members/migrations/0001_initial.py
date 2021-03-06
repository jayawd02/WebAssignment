# Generated by Django 3.1 on 2020-08-31 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_no1', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_no2', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField()),
                ('health_problems', models.TextField(blank=True, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('meal_preference', models.CharField(blank=True, choices=[('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Pescatarian', 'Pescatarian')], max_length=12, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
