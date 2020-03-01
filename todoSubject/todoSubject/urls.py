from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_main.urls')),
    path('index/', include('todo_main.urls')),
    path('home/', include('todo_main.urls')),

    # board app
    path('board/', include('todo_board.urls')),
]
