# contacts/views.py

from django.shortcuts import render
from .models import EmergencyContact

def contacts_home(request):
    contacts = EmergencyContact.objects.all()  # Get all contacts
    return render(request, 'contacts/home.html', {'contacts': contacts})
