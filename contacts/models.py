# contacts/models.py

from django.db import models

class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)          # Contact name (e.g., Campus Security)
    phone_number = models.CharField(max_length=15)   # Phone number
    service = models.CharField(max_length=100)       # Type of service (Security, Health, Counseling)

    def __str__(self):
        return f"{self.name} ({self.service})"
