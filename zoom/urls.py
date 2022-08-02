from django.urls import path
from .views import *


urlpatterns = [
    path('callback/', zoom_callback, name='zoom_call')
]