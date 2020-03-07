from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .models import TodoList
from .serializers import TodoSerializer, TodoDetailSerializer, TodoCreateSerializer


# Read- list view
class Todo_subject_restful_main(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


# Read - detail view
class Todo_subject_restful_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer


# Update
class Todo_subject_restful_update(UpdateAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


# Delete
class Todo_subject_restful_delete(DestroyAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


class TOdo_subject_restful_create(CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoCreateSerializer

'''
requests를 이용하면 기존에 db와 연동하는 것이 아닌,
rest api와 연동하여 프로그램을 작성할 수 있다.
d = {
    "title" : "파이썬에서 보냅니다",
    "content" : "파이썬!"
}
딕셔너리 데이터를 넣어주면 됨
data = requests.put('http://localhost:8088/todo_list/5/update/', data=d)
print(data)
'''
