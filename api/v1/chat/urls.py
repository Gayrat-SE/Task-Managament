from django.urls import path
from .views import ChatApi

urlpatterns = [
    path('create/', ChatApi.as_view()),
]