from django.urls import path
from . import views
from django.urls.converters import register_converter
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('register/', views.SignUp.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('reset_password/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
