# main/emergency_contacts/urls.py

from django.urls import path
from . import views

app_name = 'emergency_contacts'

urlpatterns = [
    path('', views.home, name='home'),  # List of all contacts
    path('<int:pk>/', views.contact_detail, name='contact_detail'),  # Detail page for a contact
]
