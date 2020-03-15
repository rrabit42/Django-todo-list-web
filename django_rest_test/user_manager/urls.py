from django.urls import path

from user_manager import views


urlpatterns = [
    path('login/', views.login),
    path('login/validate/', views.login_validate),
]