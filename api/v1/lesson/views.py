from lesson.models import Event
from user.models import StudentGroup
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer
)
from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import  IsAuthenticated

class CreateEvent(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =CreateEventSerializer
    queryset = Event.objects.all()




class ListLessonTeacher(ListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        teacher_lesson = Event.objects.filter(teacher_id = self.request.user.teacher.id,
            start_date__gte = self.request.GET.get('start_date'), end_date__lte = self.request.GET.get('end_date'))
        return teacher_lesson

class ListLessonStudent(ListAPIView):
    serializer_class = GetEventsSerializer
    def get_queryset(self):
        group = StudentGroup.objects.filter(student = self.request.user.student)[0]
        student_lesson = Event.objects.filter(groups = group,
            start_date__gte = self.request.GET.get('start_date'), end_date__lte = self.request.GET.get('end_date'))
        return student_lesson