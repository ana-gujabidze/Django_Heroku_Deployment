from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfileModelInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
