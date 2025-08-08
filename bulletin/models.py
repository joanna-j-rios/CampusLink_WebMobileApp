# models.py
from django.db import models  # Import the required Django model library

# Define a new model called 'Announcement'
class Announcement(models.Model):
    title = models.CharField(max_length=255)  # Store the title of the announcement (up to 255 characters)
    content = models.TextField()  # Store the content of the announcement (no character limit)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically record the date and time when the announcement is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update the time whenever the announcement is changed
    
    def __str__(self):
        return self.title  # When we print an announcement, show the title
