from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SignupForm

signup_view = CreateView.as_view(
    template_name='registration/signup.html',
    form_class=SignupForm,
    success_url=reverse_lazy('accounts:login'),
)
