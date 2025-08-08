# urls.py
from django.urls import path  # Import the 'path' function to define URLs
from . import views  # Import the views we just created

# Define the URL patterns
urlpatterns = [
    path('post/', views.post_announcement, name='post_announcement'),  # Map the '/view/' URL to the view_announcements function
    path('view/', views.view_announcements, name='view_announcements'),  # This URL handles posting announcements
]
