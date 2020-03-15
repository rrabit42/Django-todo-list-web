from django.urls import path, include

from post_service import views


urlpatterns = [
    path('', views.post_list),
    path('login/', views.login),
    path('login/validate/', views.login_validate),
]
