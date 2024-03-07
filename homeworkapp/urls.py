from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.v1),
    path('v2/', views.v2),
    path('v3/', views.v3),
]