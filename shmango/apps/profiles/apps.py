from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'shmango.apps.profiles'
    verbose_name = 'Profiles'

    def ready(self):
        import shmango.apps.profiles.signals  # noqa
