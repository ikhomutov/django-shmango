from django.db.models.signals import post_save
from django.dispatch import receiver

from shmango.apps.users.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
