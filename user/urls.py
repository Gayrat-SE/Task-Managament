from django.urls import path
from .views import *
urlpatterns = [
    path('logout', UserLogoutView.as_view(), name='logout'),

    path('student/profile', StudentProfile.as_view(), name='studentProfile'),
    path('teacher/profile', TeacherProfile.as_view(), name='teacherProfile'),
    path('admin/profile', AdminProfile.as_view(), name='adminProfile'),


    path('student-groups', Groups.as_view(), name='student-group'),
    path('student-list/<int:pk>', DetailGroup.as_view(), name='students'),

    path('teacher-list/', TeacherList.as_view(), name='teacher-list'),
    
    path('groups', StudentGroups.as_view(), name='groups'),

]