# The signal will be triggered when the user is created 
# So that the profile page is automatically created for you.

from django.contrib.auth.models import User
from django.db import models
from .models import profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save , sender = User)
def create_profile(sender , instance , created , **kwargs):
    if created:
        profile.objects.create(staff=instance)

@receiver(post_save , sender = User)
def save_profile(sender , instance  , **kwargs):
    instance.profile.save()

