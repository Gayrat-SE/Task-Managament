from gc import get_objects
from django.shortcuts import render
from user.models import StudentGroup, Student
from .models import Homework, HomeworkSubmission
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
# Create your views here.

class DetailHomework(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = "hometasks/task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_id'] = StudentGroup.objects.get(id = self.object.id)
        context['homeworks'] = Homework.objects.filter(student=self.request.user.student).exclude(homeworks__student = self.request.user.student)
        print(context['homeworks'])
        return context

def sendhomework(request):
    list_groups = StudentGroup.objects.all()
    context = {'list_groups':list_groups}
    return render(request, 'hometasks/hometask.html', context)


class CheckHomeworkGroup(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = HomeworkSubmission
    template_name: str = 'users/teacher/checkTaskGroup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checkHomeworkGroupList'] = StudentGroup.objects.filter(student__students__teacher = self.request.user.teacher).distinct()
        return context


class CheckHomeworkStudent(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/teacher/checkTaskStudent.html'
    def get_object(self, queryset=None):
        return StudentGroup.objects.get(id = self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['students'] = Student.objects.all() 
            context['Homework'] = Homework.objects.filter(teacher = self.request.user.teacher, student_group =self.get_object())
            context['group'] = self.get_object()
            return context
        except:
            return {"msg":"error"}


class GetStudentMark(LoginRequiredMixin, ListView):
    login_url = "login"
    model = HomeworkSubmission
    template_name: str = 'users/student/studentMarks.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['ratings'] = HomeworkSubmission.objects.filter(student = self.request.user.student)
            context['student'] = Student.objects.filter(id = self.request.user.student.id)[0]
        except ObjectDoesNotExist:
            return {"error":"you dont have permission"}
        return context