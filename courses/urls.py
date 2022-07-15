from django.urls import path
from .views import *


urlpatterns = [
    path('homework/<int:pk>', DetailHomework.as_view(), name='homework')
]