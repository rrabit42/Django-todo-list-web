from django import forms
from todo_board.models import TodoList


# modelForm은 MEta class에 의존하여 필드를 자동 생성
class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'end_date')