from django.db import models
from user.models import StudentGroup, Teacher
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    groups = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    zoom_join_url = models.URLField(null=True, blank=True, max_length=500)
    zoom_start_url = models.URLField(null=True, blank=True, max_length=500)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)