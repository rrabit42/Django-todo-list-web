from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from . import views
app_name = 'todo_subject_restful_main'

# router = routers.DefaultRouter()
# router.register(r'todo_board', views.Todo_subject_restful_main)
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.Todo_subject_restful_main.as_view(), name='todo_list'),
    path('todo_list/<int:no>', views.Todo_subject_restful_detail.as_view(), name='todo_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)