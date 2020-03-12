from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def post_list(request):
    template = get_template('post_service/post_list.html')
    context = {
        'python_world' : 'Python'
    }

    return HttpResponse(template.render(context))
