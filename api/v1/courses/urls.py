from django.urls import path
from .views import CreateHomework, SendHomework

urlpatterns = [
    path('homework/create/', CreateHomework.as_view()),
    path('homework/answer/', SendHomework.as_view()),
]