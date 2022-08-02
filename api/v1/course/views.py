from .serializers import (
    CreateHomeworkSerializer,
    SendHomeworkSerializer,
    SubmissionHomeworkList,
    AnswerHomeworkRating
    )
from rest_framework.generics import CreateAPIView, ListAPIView
from courses.models import (
    Homework, 
    HomeworkSubmission,
    )


class CreateHomework(CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = CreateHomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(teacher = self.request.user.teacher)


class SendHomework(CreateAPIView):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = SendHomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(student = self.request.user.student, is_answered = True)



class HomeworkSubmissions(ListAPIView):
    serializer_class = SubmissionHomeworkList
    def get_queryset(self):
        if self.kwargs["pk"]:
            submissions = HomeworkSubmission.objects.filter(homework = self.kwargs["pk"])
            return submissions


class CreateRatingAnswerHomework(CreateAPIView):
    serializer_class = AnswerHomeworkRating
    queryset = HomeworkSubmission.objects.all()