from rest_framework import serializers
from chat.models import Message



class ChatSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', 'group', 'date_added',]

    
    def create(self, validated_data):

        message = Message.objects.create(**validated_data)

        return message