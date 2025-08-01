from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) #if delete then other info wil also lost
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'self.user.username profile'
    

