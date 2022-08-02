from django.contrib import admin
from .models import Admin, Student, StudentGroup, Teacher, User
# Register your models here.

admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Teacher)
admin.site.register(User)