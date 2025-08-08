# bulletin/models.py

from django.db import models

# A simple model for an announcement
class Announcement(models.Model):
    title = models.CharField(max_length=100)  # Title of the post
    content = models.TextField()              # Message content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when post is created

    def __str__(self):
        return self.title  # Show title in admin panel and other displays
