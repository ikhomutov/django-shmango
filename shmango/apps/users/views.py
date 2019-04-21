from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import LoginForm
from .forms import SignupForm

User = get_user_model()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'


index_view = IndexView.as_view()
logout_view = LogoutView.as_view(template_name='users/logout.html')
login_view = LoginView.as_view(
    template_name='users/login.html',
    authentication_form=LoginForm
)
signup_view = CreateView.as_view(
    template_name='users/signup.html',
    form_class=SignupForm,
    success_url=reverse_lazy('users:login'),
)
password_change_view = PasswordChangeView.as_view(
    template_name='users/password_change.html',
    success_url=reverse_lazy('users:password_change_done')
)
password_change_done_view = PasswordChangeDoneView.as_view(
    template_name='users/password_change_done.html',
)
