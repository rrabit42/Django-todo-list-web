from django.urls import path

from user_manager import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/validate/', views.login_validate, name='login_validate'),
    path('join/', views.join_page, name='join'),
]