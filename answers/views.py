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

from .serializers import AnswerSerializer
import json

from .models import Answer
from random import randint

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
def get_random_answer(request):
    answer = Answer.objects.all()[randint(0, 216929)]
    serializer = AnswerSerializer(answer)
    
    return Response(serializer.data)