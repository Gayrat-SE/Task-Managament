from rest_framework import serializers
from courses.models import *
from api.v1.user.serializers import StudentListSerializer

class CreateHomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('homework_title', 'homework_file', 'homework_created_time', 'homework_deadline_time',
        'student_group', 'homework_text', 'student')


class SendHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = ('homework', 'upload_homework_time', 'submission_homework_file',)


class SubmissionHomeworkList(serializers.ModelSerializer):
    student = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = HomeworkSubmission
        fields = "__all__"
    
    def get_student(self, obj):
        user = obj.student
        serializer_user = StudentListSerializer(user, many=False)

        return serializer_user.data


class AnswerHomeworkRating(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')
    class Meta:
        model = HomeworkSubmission
        fields = ['id', 'submission_rating',]


    def create(self, validated_data):
        answer = HomeworkSubmission.objects.get(id = validated_data['id'])
        if answer.homework.homework_deadline_time < answer.upload_homework_time:
            raise serializers.ValidationError({"Time":"Time out"})
        else:
            answer.submission_rating = validated_data['submission_rating']
            answer.save()

        return answer