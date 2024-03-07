from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def v1(request):
    with open('homeworkapp/templates/homeworkapp/hw.html', 'r', encoding='utf-8') as file:
        result = file.read()
    return HttpResponse(result)


def v2(request):
    result = render_to_string('homeworkapp/hw.html')
    return HttpResponse(result)


def v3(request):
    render(request, 'homeworkapp/hw.html')
