from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=256)
    duration = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='images/')
    genres = models.ManyToManyField('Genre')

    def __str__(self): return f'Video: {self.title}'


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self): return f'Genre: {self.name}'
