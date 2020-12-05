from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Suggestion
from .serializers import suggestionSerializer

#Create your viewsets here

class SuggestionViewSet(viewsets.ModelViewSet):

    queryset = Suggestion.objects.all()
    serializer_class = suggestionSerializer