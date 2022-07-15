
from django.shortcuts import render
from users.models import StudentGroup
from .models import Homework
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class DetailHomework(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = "hometasks/taskSubmission.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['homework'] = Homework.objects.filter(student_group = self.object.id)
        return context