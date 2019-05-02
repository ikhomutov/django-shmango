from django.utils import timezone


def update_last_login(sender, user, request, **kwargs):
    user.last_login_date = timezone.now()
    user.last_login_ip = request.ip
    user.save(update_fields=('last_login_date', 'last_login_ip'))
