from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    contact_no1 = models.CharField(max_length=15, blank=True, null=True)
    contact_no2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    date_of_birth = models.DateField()
    health_problems = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    MealPreference = models.TextChoices('MealPreference', 'Vegan Vegetarian Pescatarian')
    meal_preference = models.CharField(blank=True, null=True, choices=MealPreference.choices, max_length=12)
    height = models.DecimalField(decimal_places=2, max_digits=5)
    photo = models.ImageField(blank=True, null=True)
    Gender = models.TextChoices('Gender', 'Male Female Other')
    gender = models.CharField(blank=True, null=True, choices=Gender.choices, max_length=6)

    def __str__(self):
        return self.first_name


class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=25)
    PlanType = models.TextChoices('PlanType', 'Individual Group Couple Family Corporate')
    plan_type = models.CharField(choices=PlanType.choices, max_length=12)
    DurationChioces = models.TextChoices('DurationChoice', '1-month 3-months 6-months 1-year')
    duration = models.CharField(choices=DurationChioces.choices, max_length=10)
    fee = models.DecimalField(decimal_places=2, max_digits=10)
    ActiveStatus = models.TextChoices('ActiveStatus', 'Active Inactive')
    status = models.CharField(choices=ActiveStatus.choices, default='Active', max_length=10)

    def __str__(self):
        return self.plan_name


class Membership(models.Model):
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.PROTECT)
    customers=models.ManyToManyField(Member)
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.DecimalField("discount percentage", decimal_places=2, max_digits=5, default=0)
    final_fee = models.DecimalField(decimal_places=2, max_digits=10)
