# contacts/views.py

from django.shortcuts import render, redirect  # add redirect import
from .models import EmergencyContact
from .forms import EmergencyContactForm  # import the form we created

def contacts_home(request):
    contacts = EmergencyContact.objects.all()  # Get all contacts
    return render(request, 'contacts/home.html', {'contacts': contacts})

def add_contact(request):
    # This view handles displaying the form and saving new contacts
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)  # Get data from form submission
        if form.is_valid():                         # Validate form data
            form.save()                            # Save new EmergencyContact to DB
            return redirect('contacts_home')      # Redirect back to contacts list page
    else:
        form = EmergencyContactForm()              # Show empty form on GET request
    
    # Render the form page, passing form object to template
    return render(request, 'contacts/add_contact.html', {'form': form})
