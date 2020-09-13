from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    TypeChoices = models.TextChoices('TypeChoices', 'Exercise Meal-Prep Recipe Other')
    type = models.CharField(choices=TypeChoices.choices, max_length=12)
    thumbnail= models.ImageField(blank=True, null=True, upload_to='video_thumbnail',default='youtube-default.jpg')
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add= True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url (self): # setting return url when create video is submitted
        return reverse('video-detail',kwargs={'pk': self.pk})  #return full path as string


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
    date_posted = models.DateTimeField(auto_now_add= True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url (self): # setting return url when create post is submitted
        return reverse('recipe-detail',kwargs={'pk': self.pk})  #return full path as string

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add= True) #auto_now_add= True. date modified ->auto_now=True
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='post_pics')

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dislikes(self):
        return self.dislikes.users.count()

    def __str__(self):
        return str(self.content)[:30]

    def get_absolute_url (self): # setting return url when create post is submitted
        return reverse('post-detail',kwargs={'post_id': self.pk})  #return full path as string



class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class PostLike(models.Model):
    post = models.OneToOneField(Post, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.content)[:30]

class PostDislike(models.Model):
    post = models.OneToOneField(Post, related_name="dislikes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='post_dislikes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.content)[:30]