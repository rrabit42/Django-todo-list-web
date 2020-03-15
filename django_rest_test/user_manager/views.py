from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user_manager.forms import LoginForm


def login(request):
    context = {
        'login_form': LoginForm()
    }
    return render(request, 'user_manager/login_form.html', context)


# 인증을 위한 다양한 모듈이 있는 django.contrib.auth
def login_validate(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        # authenticate() 함수는 username과 password 등, 여러가지 파라메터를 통하여 인증 과정을 수행하게 됩니다.
        # django.contrib.auth.models 에 포함된 User 모델의 데이터로 검증을 수행하게 되죠.
        # 일단, request로 넘어오는 데이터를 LoginForm 으로 받아서 폼 검증 과정을 Form 클래스에 전담시키고, 그 안에 있는 내용을 통하여 인증을 하게 코드를 짭니다.
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])
        # 기본적인 예외들
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/board/')
        else:
            return HttpResponse('사용자가 없거나 비밀번호를 잘못 누르셨습니다.')
    else:
        return HttpResponse('로그인 폼이 비정상적입니다.')
    return HttpResponse('알 수 없는 오류입니다.')
