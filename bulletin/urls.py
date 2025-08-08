# urls.py
from django.urls import path  # Import the 'path' function to define URLs
from . import views  # Import the views we just created

app_name = 'bulletin'  # Make sure this is set

# Define the URL patterns
urlpatterns = [
    path('view/', views.view_announcements, name='view_announcements'),
    path('post/', views.post_announcement, name='post_announcement'),
    path('search/', views.search_announcements, name='search_announcements'),  # Add this line for search
]