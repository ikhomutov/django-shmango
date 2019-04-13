from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import LoginForm
from .forms import SignupForm

User = get_user_model()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        form.save()
        return super().form_valid(form)


logout_view = LogoutView.as_view(template_name='users/logout.html')
login_view = LoginView.as_view(
    template_name='users/login.html',
    authentication_form=LoginForm
)
signup_view = SignupView.as_view()
