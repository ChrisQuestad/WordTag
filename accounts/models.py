from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    photo = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    user = kwargs['instance']
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=kwargs['instance'])
