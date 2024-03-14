from django.urls import path
from . import views
from django.urls.converters import register_converter

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/<int:user_id>/posts', views.user_posts, name='user_posts'),
    path('post/<int:post_id>', views.post, name='post'),
]
