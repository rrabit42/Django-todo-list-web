from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

# 응답에 여러가지 헤더가 포함되어져야 하는데, 이를 쉽고 간편하게 처리해주는 HttpResponse를 장고에서 제공해주고 있음
# 따라서 우리는 간단하게 return HttpResponse(데이터) 모양으로 쉽게 응답을 보낼 수 있음
def blog_page(request):
    post_list = Post.objects.all()

    return HttpResponse('Hello ' + post_list[0].title)
