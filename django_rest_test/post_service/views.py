from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from post_service.models import Post


def post_list(request):
    page_data = Paginator(Post.objects.all().order_by('title'), 5)
    page = request.GET.get('page') # GET parameter로 page가 온다고 가정하고 데이터들을 건들임

    if page is None:
        page = 1

    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = {
        'post_list': posts,
        'current_page': int(page),
        'total_page': range(1, page_data.num_pages + 1)
    }
    return render(request, 'post_service/post_list.html', context)
