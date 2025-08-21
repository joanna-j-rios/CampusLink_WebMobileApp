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
from activities import views as activities_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the URLs from the activities app. This covers login, register, logout, tasks, delete, toggle, AND home_view.
    path('activities/', include('activities.urls')),
    
    # Include the URLs from the bulletin app.
    path('bulletin/', include('bulletin.urls')),  
    
    # Include the urls from the emergency_contacts app (assuming it exists).
    # If emergency_contacts app does not exist, you can remove this line.
    path('emergency-contacts/', include('emergency_contacts.urls')),  
    
    # CRITICAL FIX: Set the root URL (e.g., http://127.0.0.1:8000/) to directly use the home_view from activities.
    # The home_view itself already has @login_required, which will redirect unauthenticated users to login.
    path('', activities_views.home_view, name='home_root'),
]
