from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse

from . import constants
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True, blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_blocked = models.BooleanField(default=False)
    block_comment = models.CharField(max_length=255, blank=True)
    block_reason = models.PositiveSmallIntegerField(
        choices=constants.BLOCK_REASONS,
        default=constants.NONE
    )
    date_blocked = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    @property
    def is_active(self):
        return not self.is_blocked

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.id})


