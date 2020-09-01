from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    contact_no1 = models.CharField(max_length=15, blank=True, null=True)
    contact_no2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField()
    health_problems = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    MealPreference = models.TextChoices('MealPreference', 'Vegan Vegetarian Pescatarian')
    meal_preference = models.CharField(blank=True, null=True, choices=MealPreference.choices, max_length=12)
    height = models.DecimalField(decimal_places=2, max_digits=5)
    photo = models.ImageField(blank=True, null=True)
    Gender = models.TextChoices('Gender', 'Male Female Other')
    gender = models.CharField(blank=True, null=True, choices=Gender.choices, max_length=6)


class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=25)
    PlanType = models.TextChoices('PlanType', 'Individual Group Couple Family Corporate')
    plan_type = models.CharField(choices=PlanType.choices, max_length=12)
    duration = models.DurationField(name='duration (months)') #todo change the type
    fee = models.DecimalField(decimal_places=2, max_digits=10)
    ActiveStatus=models.TextChoices('ActiveStatus' , 'Active Inactive')
    status = models.CharField(choices=ActiveStatus.choices, default='Active', max_length=10)
