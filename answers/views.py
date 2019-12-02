from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .serializers import AnswerSerializer, EpisodeSerializer
import json

from .models import Answer, Episode

class AnswerViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


def index(request):
    return HttpResponse("Hello, world. You're at the answers index.")

@csrf_exempt
@api_view(['POST'])
def fetch_answers_by_show(request):
    pass

@csrf_exempt
@api_view(['GET'])
def get_show_numbers(request):
    pass

@csrf_exempt
@api_view(['GET'])
def get_episodes(request):
    episodes = Episode.objects.all()
    serializer = EpisodeSerializer(episodes, many=True)
    return Response(serializer.data)
