from user.models import StudentGroup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import  Message





class Chat(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Message
    template_name: str = 'chat/room.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentGroup.objects.filter(student = self.request.user.student)[0]
        context['messages'] = Message.objects.filter(group = context['student'])

        return context