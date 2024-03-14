from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author
from .forms import PostForm, AuthorForm


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'myapp/about.html', {'title': 'О нас'})


def user_posts(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(pk=user_id)
            Post(**form.cleaned_data, author=author).save()
    else:
        form = PostForm()

    user = get_object_or_404(Author, pk=user_id)
    posts = Post.objects.filter(author=user)
    context = {
        "title": "Посты",
        "author": user,
        "posts": posts,
        'form': form,
        'message': 'Это пример собственных фильтров'
    }
    return render(request, 'myapp/posts.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.views += 1
    post.save()
    context = {
        "post": post,
    }
    return render(request, 'myapp/post.html', context)


# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу данных.
# Используйте ранее созданную модель Author
def authors(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Author(**form.cleaned_data).save()
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {
        "title": "Авторы",
        "authors": authors,
        'form': form,
    }
    return render(request, 'myapp/authors.html', context)
