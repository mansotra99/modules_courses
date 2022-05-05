from rest_framework import serializers

from .models import *


class MouduleSerializer(serializers.ModelSerializer):
    
    def __init__(self, user_id):
        self.user_id = user_id

    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return UserModule.objects.get(user_id=self.user_id, module_id=obj.id).last()

    class Meta:
        model = Module
        fields = ['id', 'title','description','estimated_time_to_complete','points', 'status']


class ChapterSerializer(serializers.ModelSerializer):
    estimated_time_to_complete = serializers.CharField(source='module.estimated_time_to_complete')
    points = serializers.CharField(source='module.points')

    class Meta:
        model = Chapter
        fields = ['id', 'module_id', 'title', 'description']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','module_id','points','question','options']

# answer_explanation
# answer_option