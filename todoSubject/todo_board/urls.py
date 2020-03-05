from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views


app_name = 'todo_board'

urlpatterns = [
    path('', views.Todo_main.as_view(), name='todo_board'),
    path('insert/', views.check_post, name='todo_board_insert'),
    path('<int:pk>/detail/', views.Todo_board_detail.as_view(), name='todo_board_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)