"""
This file powers creation of all forms. You will need to modify
the SignUpForm in order to start collecting the distinct_id.
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','first_name', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass
    class Meta:
        model = User
        fields = ('username', 'password')
