from django.views.generic import CreateView
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('dice:home')
    template_name = 'users/signup.html'


class MyLoginView(LoginView):
    # form_class = CreationForm
    success_url = reverse_lazy('dice:home')
    template_name = 'users/signup.html'

    def get_success_url(self):
        return self.success_url
#
#
# class LogoutView(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('dice:home')
#     template_name = 'users/signup.html'
