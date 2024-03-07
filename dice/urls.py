from django.urls import path
from . import views

urlpatterns = [
    path('dice/', views.dice),
    path('coin', views.coin),
    path('hundred', views.hundred),
]