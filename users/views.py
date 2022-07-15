from django.shortcuts import render
from courses.models import Homework
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.

class LoginUser(LoginView):
    template_name: str = "users/login.html"
    def get_success_url(self):
        success_url = reverse_lazy("index")
        return success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class Dashboard(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
    
        return render(request, 'index.html')


class Groups(LoginRequiredMixin, ListView):
    login_url = "login"
    context_object_name = "groups"
    model = StudentGroup
    template_name: str = 'users/student/studentGroup_list.html'
        

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


class StudentGroups(LoginRequiredMixin, ListView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/student/groups.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['groups'] = StudentGroup.objects.filter(student = self.request.user.student.id)
            for group in context['groups']:
                context['homeworks'] = Homework.objects.filter(student_group = group)
            return context
        except:
            return {"msg":"error"}