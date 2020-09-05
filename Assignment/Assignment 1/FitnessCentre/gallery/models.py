from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    TypeChoices = models.TextChoices('TypeChoices', 'Exercise Meal-Prep Recipe Other')
    type = models.CharField(choices=TypeChoices.choices, max_length=12)
    thumbnail= models.ImageField(blank=True, null=True, upload_to='video_thumbnail',default='youtube-default.jpg')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    MealType = models.TextChoices('MealType', 'Vegan Vegetarian Seafood Meat Other')
    type = models.CharField(blank=True, null=True, choices=MealType.choices, max_length=12)
    MealCategory = models.TextChoices ('MealCategory', 'Main Snack Side Soup Salad Dessert Drink Other')
    category = models.CharField(blank=True,null=True, choices=MealCategory.choices, max_length=10)
    description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe_pics',blank=True,null=True, default='recipe-default.jpg')
    ingredients = models.TextField()
    prep_time = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='post_pics')

    def __str__(self):
        return self.content

    def get_absolute_url (self): # setting return url when create post is submitted
        return reverse('post-detail',kwargs={'pk': self.pk})  #return full path as string

