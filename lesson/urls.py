from django.urls import path
from .views import *
urlpatterns = [
    path('calendar', StudentCalendar.as_view(), name='calendar'),
    path('teacher/calendar', TeacherCalendar.as_view(), name='teacherCalendar')
]