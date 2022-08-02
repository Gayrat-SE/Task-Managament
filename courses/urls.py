from django.urls import path
from .views import *
urlpatterns = [
    path('homework/<int:pk>', DetailHomework.as_view(), name='homework'),
    path('homework/create', sendhomework, name='sendhomework'),
    path('check/homeworks', CheckHomeworkGroup.as_view(), name='checkhomeworkgroup'),
    path('detail/students/<int:pk>', CheckHomeworkStudent.as_view(), name='checkhomeworkstudent'),
    path('rating/', GetStudentMark.as_view(), name='rating'),
]