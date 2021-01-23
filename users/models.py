from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile_images/')
    # profile_image = models.ImageField(default='default.jpg', upload_to='images/profile_images/')
    website_url = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    pinterest_url = models.CharField(max_length=100, null=True, blank=True)
    linkedin_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

