from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import LoginForm

User = get_user_model()


logout_view = LogoutView.as_view(template_name='accounts/logout.html')
login_view = LoginView.as_view(
    template_name='accounts/login.html',
    authentication_form=LoginForm
)
password_change_view = PasswordChangeView.as_view(
    template_name='accounts/password_change.html',
    success_url=reverse_lazy('accounts:password_change_done')
)
password_change_done_view = PasswordChangeDoneView.as_view(
    template_name='accounts/password_change_done.html',
)
