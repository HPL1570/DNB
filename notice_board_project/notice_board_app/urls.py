# notice_board_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message_page, name='message_page'),
    path('display/', views.display_page, name='display_page'),
]
