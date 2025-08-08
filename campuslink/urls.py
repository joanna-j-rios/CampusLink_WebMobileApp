# campuslink/urls.py
from django.contrib import admin
from django.urls import path, include  # Import 'include' to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulletin/', include('bulletin.urls')),  # Add this line to include bulletin app URLs
]
