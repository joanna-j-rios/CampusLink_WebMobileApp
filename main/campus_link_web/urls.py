"""
URL configuration for campus_link_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    # This path handles the root URL (e.g., http://127.0.0.1:8000/)
    # It redirects all requests to the 'login' URL, which we defined in activities/urls.py
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='home'),
    path('admin/', admin.site.urls),
    
    # The 'include' function references the urls.py file from the activities app.
    # All URLs that start with 'activities/' will be handled by the activities app.
    path('activities/', include('activities.urls')),
    # Include the URLs from the bulletin app.
    path('bulletin/', include('bulletin.urls')),  
    # Include the urls from the emergency_contacts app
    path('emergency-contacts/', include('emergency_contacts.urls')),  
]
