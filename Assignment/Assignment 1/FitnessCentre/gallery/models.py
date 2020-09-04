from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    TypeChoices = models.TextChoices('TypeChoices', 'Exercise Meal-Prep Recipe Other')
    type = models.CharField(choices=TypeChoices.choices, max_length=12)


class RecipeImage(models.Model):
    name = models.CharField(max_length=50)
    MealType = models.TextChoices('MealType', 'Vegan Vegetarian Seafood Meat Other')
    type = models.CharField(blank=True, null=True, choices=MealType.choices, max_length=12)
    description = models.TextField()
    recipe_image = models.ImageField()
    ingredients = models.TextField()
    prep_time = models.SmallIntegerField()
