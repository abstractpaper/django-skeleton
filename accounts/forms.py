from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import User

class LoginForm(AuthenticationForm):
    next = forms.CharField(widget=forms.HiddenInput(), initial=reverse_lazy('home'))

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that password "
            "field is case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }