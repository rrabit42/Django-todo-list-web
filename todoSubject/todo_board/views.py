from django.shortcuts import render, redirect
from django.views import View, generic

from todo_board.forms import TodoForm
from todo_board.models import TodoList


class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_list.html'
        todo_list = TodoList.objects.all()
        return render(request, template_name, {"todo_list" : todo_list})


def check_post(request):
    template_name = 'todo_board/todo_board_success.html'
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # commit=False를 하게 되면 데이터베이스에 당장 저장 X, 즉 DB에 데이터를 저장하기 전에 특정 행위를 하고 싶을 때 사용
            todo.todo_save()
            message = "일정을 추가하였습니다."
            return render(request, template_name, {"message": message})

    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form": form})