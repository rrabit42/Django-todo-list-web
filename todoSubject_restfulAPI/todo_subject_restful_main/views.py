from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import TodoList
from .serializers import TodoSerializer, TodoDetailSerializer


# list view
class Todo_subject_restful_main(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


# detail view
class Todo_subject_restful_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer