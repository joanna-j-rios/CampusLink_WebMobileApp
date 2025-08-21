from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmergencyContact

@login_required
def home(request):
    contacts = EmergencyContact.objects.all()
    return render(request, 'emergency_contacts/home.html', {'contacts': contacts})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    return render(request, 'emergency_contacts/detail.html', {'contact': contact})
