# forms.py

from django import forms
from django.contrib.auth.models import User

# This form is for the login process.
class CustomLoginForm(forms.Form):
    # This form only needs a username and password field.
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# This form is for the registration process.
class CustomRegistrationForm(forms.Form):
    # This form only needs a username and password field.
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    # This method checks that the username is not already taken.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in use.")
        return username

