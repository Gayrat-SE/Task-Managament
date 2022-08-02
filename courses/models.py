from user.models import *
from base.models import Base
import os
from django.core.validators import FileExtensionValidator
from datetime import datetime
import pytz
from rest_framework.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator



def deadline_time(value):

    if value < datetime.now(pytz.utc):
        raise ValidationError("Error Time")



class Homework(Base):
    homework_title = models.CharField(max_length=255)
    homework_text = models.TextField(blank=True)
    homework_file = models.FileField(upload_to='homeworks/questions/group/')
    homework_created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    homework_deadline_time = models.DateTimeField(validators=[deadline_time])
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT, related_name='groups', blank=True, null=True)
    student = models.ManyToManyField(Student, blank=True, related_name='students')

    def filename(self):
        return os.path.basename(self.homework_file.name)







class HomeworkSubmission(Base):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='homeworks')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='answer_student')
    upload_homework_time = models.DateTimeField(auto_now_add=True)
    submission_homework_file = models.FileField(upload_to='homeworks/answers/', blank=True, 
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx", "ppt"])])
    submission_rating = models.IntegerField(blank=True, validators=[MaxValueValidator(5), MinValueValidator(0)], null=True)
    is_answered = models.BooleanField(default=False)
    def filename(self):
        return os.path.basename(self.submission_homework_file.name)