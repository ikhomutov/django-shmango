from .models import Profile


def create_profile(backend, user, *args, **kwargs):
    profile = Profile(
        user=user,
        subscribed=True,
    )
    profile.save()
