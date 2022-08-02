from django.urls import path

from .views import Chat

urlpatterns = [

    path('', Chat.as_view(), name='room'),
]