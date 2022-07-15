from django.urls import path
from .views import *
urlpatterns = [
    path('student/create/', StudentCreate.as_view()),
    path('teacher/create/', TeacherCreate.as_view()),
    path('student/list/', StudentList.as_view()),
    path('group/list/', StudentGroupList.as_view()),
    path('group/detail/<int:pk>/', StudentGroupDetailList.as_view()),
    path('update/student/<int:pk>/', StudentUpdate.as_view()),
    path('group/create/', StudentGroupCreate.as_view()),
    ]