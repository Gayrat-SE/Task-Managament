from django.urls import path
from .views import *
urlpatterns = [
    path('student/create/', StudentCreate.as_view()),
    path('teacher/create/', TeacherCreate.as_view()),
    path('admin/create/', AdminCreate.as_view()),
    path('student/list/', StudentList.as_view()),
    path('group/list/', StudentGroupList.as_view()),
    path('group/detail/<int:pk>/', StudentGroupDetailList.as_view()),
    path('student/update/<int:pk>/', StudentUpdate.as_view()),
    path('group/create/', StudentGroupCreate.as_view()),
    path('teacher/update/<int:pk>/', TeacherUpdate.as_view()),
    path('group/detail/<int:pk>/', StudentGroupDetailList.as_view()),
    path('admin/update/<int:pk>/', AdminUpdate.as_view()),
    ]