from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        required=False,
    )
    last_name = forms.CharField(
        label='Last Name',
        required=False,
    )
    email = forms.EmailField(
        label='Email',
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
    )
    subscribed = forms.BooleanField(
        label="I'd like to receive news and offers",
        required=False
    )

    class Meta:
        model = User
        fields = (
            'email',
        )

    def save(self, **kwargs):
        user = super().save(**kwargs)
        profile = user.profile
        profile.first_name = self.cleaned_data.get('first_name')
        profile.last_name = self.cleaned_data.get('last_name')
        profile.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }
        ),
    )

    error_messages = {
        'invalid_login':
            'Please enter a correct email and password. Note that both '
            'fields may be case-sensitive.'
        ,
        'inactive': 'This account is inactive.',
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'], code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'], code='invalid_login',
        )
