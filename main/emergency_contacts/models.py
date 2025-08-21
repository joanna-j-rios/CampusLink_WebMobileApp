from django.db import models

class EmergencyContact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
