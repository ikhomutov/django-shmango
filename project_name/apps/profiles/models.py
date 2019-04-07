from django.db import models

from . import constants


class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=constants.GENDERS,
        default=constants.GENDER_NONE,
    )

    def get_full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def get_short_name(self):
        return self.first_name

