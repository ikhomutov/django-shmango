from django.contrib.auth import get_user_model
from django.db import models

from . import constants

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=constants.GENDERS,
        default=constants.GENDER_NONE,
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def get_short_name(self):
        return f'{self.first_name}'
