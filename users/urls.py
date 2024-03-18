from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('register/', views.SignUp.as_view()),
    path('login/', views.MyLoginView.as_view(), name='login'),
    # path('reset_password/', LoginView.as_view(tempate_name='users/reset_password.html')),
    # path('logout/', LogoutView.as_view(tempate_name='users/logout.html')),
]
