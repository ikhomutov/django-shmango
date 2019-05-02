from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in


class AccountsConfig(AppConfig):
    name = 'shmango.apps.accounts'
    verbose_name = 'Accounts'

    def ready(self):
        from .signals import update_last_login
        user_logged_in.connect(
            update_last_login, dispatch_uid='update_last_login'
        )
