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


class Todo_board_detail(generic.DetailView):
    model = TodoList
    template_name = 'todo_board/todo_board_detail.html'
    context_object_name = 'todo_list' # 해당 object의 이름을 설정, 그래서 template에 저 이름을 가지고 접근


# django는 generic.UpdateView로 수정과 관련된 뷰를 제공
# update와 관련된 기능을 제공해주기에 save 기능과 form 데이터를 받아오는 기능이 필요
# 왜냐하면 수정할 때 게시판에서 작성한 글을 가지고 와서 update 해야하기 때문
# model은 똑같은 todolist, fields로는 title, content, date를 받고
# form이 유요하면 form_valid 함수 실행, 그리고 form.save()를 통해 저장
class Todo_board_update(generic.UpdateView):
    model = TodoList
    fields = ('title', 'content', 'end_date') # 이 모델의 필드만 써줄 것이다.
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/' # data 업데이트에 성공할 경우 이동할 url

    def form_valid(self, form):
        form.save()
        return render(self.request, 'todo_board/todo_board_success.html', {"message": "일정을 업데이트 했습니다."})

    def get(self, request, *args, **kwargs):
        # 오브젝트를 받아와서 폼 클래스를 받아온 후 이것을 return 해줘야한다.
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
'''
get으로 수정페이지에 들어간다면(수정완료 버튼을 누른 상태X, 수정 버튼을 눌렀을 때 나오는 페이지)
기존에 작성한 내용이 적용되어 있어야함 그래서 object를 받아오고 get_form_class를 통해 폼을 가져옴
이후 get_context_data를 통해 context를 만들고 render_to_response를 해주면 그 전에 있던 값이 적용됨
'''