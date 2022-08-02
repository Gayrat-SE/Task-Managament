from urllib import request
from courses.models import Homework
from .models import *
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
# Create your views here.


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class TeacherProfile(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "user"
    model = User
    template_name: str = "users/teacher/teacherProfile.html"

class StudentProfile(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "user"
    model = User
    template_name: str = "users/student/studentProfile.html"

class AdminProfile(LoginRequiredMixin, ListView):
    login_url = "login"
    model = User
    template_name: str = "users/admin/adminProfile.html"






class Groups(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "groups"
    model = StudentGroup
    template_name: str = 'users/student/studentGroup_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.filter(student_list__isnull = True)

        return context

class DetailGroup(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/student/studentList.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentGroup.objects.filter(id=self.object.id)
        return context

class TeacherList(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Teacher
    template_name: str = 'users/teacher/teacherList.html'
    context_object_name = "teachers"


class StudentGroups(LoginRequiredMixin, ListView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/student/groups.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['groups'] = StudentGroup.objects.filter(student = self.request.user.student.id)
            context['homeworks'] = Homework.objects.filter(student = self.request.user.student).exclude(homeworks__student = self.request.user.student)
            return context
        except ObjectDoesNotExist:
            return {"msg":"error"}

