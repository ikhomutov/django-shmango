from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

User = get_user_model()


login_view = LoginView.as_view(template_name='users/login.html')
logout_view = LogoutView.as_view(template_name='users/logout.html')
