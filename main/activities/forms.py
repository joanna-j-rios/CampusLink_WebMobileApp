# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Task # Ensure Task model is imported

# This form is for the login process.
class CustomLoginForm(forms.Form):
    # This form only needs a username and password field.
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

# This form is for the registration process.
class CustomRegistrationForm(forms.Form):
    # This form only needs a username and password field.
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Choose a Password'})
    )

    # This method checks that the username is not already taken.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in use.")
        return username

class TaskForm(forms.ModelForm):
    class Meta:
             model = Task
             fields = ['task_name', 'description', 'due_date', 'is_completed']
             widgets = {
                 # CHANGED: 'task_name' is now a single-line TextInput
                 'task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Name'}),
                 'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Task Description'}),
                 'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                 'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
              }
