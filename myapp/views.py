from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'myapp/about.html', {'title': 'О нас'})


def user_posts(request, user_id):
    user = get_object_or_404(Author, pk=user_id)
    posts = Post.objects.filter(author=user)
    context = {
        "title": "Посты",
        "author": user,
        "posts": posts
    }
    return render(request, 'myapp/posts.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    context = {
        "post": post,
    }
    return render(request, 'myapp/post.html', context)
