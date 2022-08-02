from .serializers import *
from rest_framework import generics
from user.models import *
from rest_framework.permissions import IsAuthenticated


class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAuthenticated]
    

class StudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer




class StudentGroupCreate(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [IsAuthenticated]



class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentGroupList(generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer


class StudentGroupDetailList(generics.RetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer

class AdminCreate(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAuthenticated]

class AdminUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer



        