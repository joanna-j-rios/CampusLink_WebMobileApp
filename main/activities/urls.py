# activities/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'), # New: URL for the home screen
    path('tasks/', views.tasks_view, name='tasks'),
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('task/toggle_complete/<int:pk>/', views.toggle_task_complete, name='toggle_task_complete'),
]
