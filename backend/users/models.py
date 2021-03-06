from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
         if created:
             Token.objects.create(user=instance)

    # def save(self,*args,**kwargs): # resizing the profile pic
    #      super().save(*args,**kwargs)
    #
    #      img = Image.open(self.profile_pic.path)
    #
    #      if img.height > 300 or img.width > 300:
    #          output_size = (300,300)
    #          img.thumbnail(output_size)
    #          img.save(self.profile_pic.path)
