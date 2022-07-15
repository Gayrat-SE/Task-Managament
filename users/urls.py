from django.urls import path
from .views import *
urlpatterns = [
    path('', LoginUser.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('dashboards/', Dashboard.as_view(), name='index'),

    path('student-groups/', Groups.as_view(), name='student-group'),
    path('student-list/<int:pk>', DetailGroup.as_view(), name='students'),

    path('teacher-list/', TeacherList.as_view(), name='teacher-list')
    ,
    path('groups/', StudentGroups.as_view(), name='groups')
]