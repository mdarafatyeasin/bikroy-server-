from django.shortcuts import render
from rest_framework import viewsets
from .models import addModel
from .serializers import addSerializer

# Create your views here.
class addViewSets(viewsets.ModelViewSet):
    queryset = addModel.objects.all()
    serializer_class = addSerializer