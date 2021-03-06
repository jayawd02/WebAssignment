# Generated by Django 3.1.1 on 2020-09-05 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_workoutplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')], max_length=10)),
                ('serving_size', models.CharField(max_length=20)),
                ('calories', models.PositiveSmallIntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plans.meal')),
            ],
        ),
    ]
