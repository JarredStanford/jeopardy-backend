from rest_framework.serializers import ModelSerializer
from .models import Answer, Episode

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class EpisodeSerializer(ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'