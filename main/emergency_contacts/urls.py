# main/emergency_contacts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency_contacts_view, name='emergency_contacts'),
]