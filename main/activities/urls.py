# activities/urls.py

from django.urls import path
from . import views

# This list contains the URL patterns for the 'activities' app.
urlpatterns = [
    # This path matches the base URL for the activities app (e.g., /activities/).

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.tasks_view, name='tasks'),
]
