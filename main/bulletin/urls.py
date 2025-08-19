# campuslink_web/bulletin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.bulletin_board_view, name='bulletin_board'),
]
