from django.shortcuts import render, redirect
from django.views import View, generic
from todo_board.models import TodoList


class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_list.html'
        todo_list = TodoList.objects.all()
        return render(request, template_name, {"todo_list" : todo_list})

