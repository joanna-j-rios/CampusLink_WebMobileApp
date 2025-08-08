from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Use Django's built-in LoginView with your custom template
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),

    # Optional: Add logout path too
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
