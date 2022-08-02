from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from user.models import *
from courses.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

class LoginUser(LoginView):
    template_name: str = "users/login_simple.html"
    def get_success_url(self):
        success_url = reverse_lazy("index")

        return success_url


class Dashboard(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        student_count = Student.objects.all().count()
        teacher_count = Teacher.objects.all().count()
        user_count = User.objects.all().count()
        try:
            answer = HomeworkSubmission.objects.filter(student = request.user.student.id).count()
            homework = Homework.objects.filter(student_group__student = request.user.student.id).exclude(homeworks__student = request.user.student).count()
            context = {
                "answer":answer,
                "homework":homework,
                "student_count":student_count,
                "teacher_count":teacher_count,
                "user_count":user_count,
            }
            return render(request, 'index.html', context=context)
        except ObjectDoesNotExist:
            group = StudentGroup.objects.all()
            context = {
                "student_count":student_count,
                "teacher_count":teacher_count,
                "user_count":user_count,
                'groups':group
            }
            return render(request, 'index.html', context=context)