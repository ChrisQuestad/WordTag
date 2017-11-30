from django.db import models

class Profile(models.Model):
    photo = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
