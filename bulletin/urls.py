# bulletin/urls.py

from django.urls import path
from . import views  # Make sure 'views' is imported from this app

urlpatterns = [
    path('', views.bulletin_home, name='bulletin_home'),  # Main page for announcements
    path('post/', views.post_announcement, name='post_announcement'),  # Form to post a new announcement
]
