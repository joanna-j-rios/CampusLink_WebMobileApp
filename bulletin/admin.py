# bulletin/admin.py

from django.contrib import admin
from .models import Announcement

# Show announcements in the admin panel
admin.site.register(Announcement)
