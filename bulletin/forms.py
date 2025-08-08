# forms.py
from django import forms  # Import Django forms
from .models import Announcement  # Import the Announcement model

# Create a form class for announcements
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement  # Use the Announcement model for this form
        fields = ['title', 'content']  # These are the fields the user will fill out
