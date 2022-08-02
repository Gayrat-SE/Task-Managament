from lesson.models import Event
from rest_framework import serializers
import requests
import json
from datetime import  datetime
import pytz
from rest_framework.exceptions import ValidationError
from api.v1.user.serializers import TeacherListSerializer, StudentGroupListSerializer


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date',  'groups')


    def validate(self, attrs):
        if attrs["end_date"] < datetime.now(pytz.utc):
            raise ValidationError({"error":"Error Time"})

        return attrs


    def create(self, validated_data):
        lesson = Event.objects.create(groups = validated_data['groups'], title = validated_data['title'], start_date = validated_data['start_date'],
            end_date = validated_data['end_date'], teacher_id = self.context['request'].user.teacher.id)
        data = requests.post("https://api.zoom.us/v2/users/me/meetings", 
            headers={
                "Authorization": f"Bearer { self.context['request'].session['zoom_access_token'] } ",
                "content-type": "application/json"
            }, 
            data=json.dumps({
                "topic": f"Interview with { lesson.groups.name }",
                "type": 2,
                "start_time": validated_data['end_date'],
            }, default=str))

        lesson.zoom_join_url = data.json()["join_url"]
        lesson.zoom_start_url = data.json()["start_url"]

        lesson.save()
        return lesson






class GetEventsSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField(read_only = True)
    teacher = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'groups', 'teacher', 'zoom_join_url',)

    def get_groups(self, obj):

        id = obj.groups
        serializer = StudentGroupListSerializer(id, many = False)

        return serializer.data
    
    def get_teacher(self, obj):

        user = obj.teacher
        serializer = TeacherListSerializer(user, many = False)
        return serializer.data



