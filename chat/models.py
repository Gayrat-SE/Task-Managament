from django.db import models
from user.models import StudentGroup, Teacher, Student
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    group = models.ForeignKey(StudentGroup, related_name='messages', on_delete=models.PROTECT, blank=True, null=True)
    content = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added',)