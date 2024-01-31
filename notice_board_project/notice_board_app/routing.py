# notice_board_app/routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notice_board/$', consumers.NoticeBoardConsumer.as_asgi()),
]
