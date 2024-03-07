from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    result = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    
    <h1>Главная Страница</h1>
    <p>
        <a href="about">О нас</a>
    </p>
    </body>
    </html>
    """

    return HttpResponse(result)


def about(request):
    return HttpResponse("About us")
