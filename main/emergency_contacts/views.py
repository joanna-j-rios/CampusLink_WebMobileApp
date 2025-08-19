from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def emergency_contacts_view(request):
    """
    Renders the emergency contacts page.
    """
    return render(request, 'emergency_contacts/emergency_contacts.html')