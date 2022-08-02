from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('course/', include('api.v1.course.urls')),
    path('lesson/', include('api.v1.lesson.urls')),
    path('chat/', include("api.v1.chat.urls")),
    ]