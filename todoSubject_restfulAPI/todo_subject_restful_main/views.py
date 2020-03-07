from django.shortcuts import render
from rest_framework import viewsets

from .models import TodoList
from .serializers import TodoSerializer


class Todo_subject_restful_main(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer