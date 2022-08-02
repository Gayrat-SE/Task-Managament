from django.urls import path

from .consumers import ChatStudent

websocket_urlpatterns = [
    path('ws/chat/<int:room_name>/', ChatStudent.as_asgi()),
]