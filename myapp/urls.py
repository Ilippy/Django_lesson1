from django.urls import path
from . import views
from .converters import MySlug
from django.urls.converters import register_converter

register_converter(MySlug, 'my_slug')

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/<int:user_id>/posts', views.user_posts, name='user_posts'),
    path('post/<my_slug:slug>', views.post, name='post'),
    path('authors', views.authors),
]
