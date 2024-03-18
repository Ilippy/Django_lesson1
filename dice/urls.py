from django.urls import path
from . import views

app_name = 'dice'

urlpatterns = [
    # path('dice/', views.dice),
    # path('coin/<int:amount_flips>', views.coin),
    # path('hundred/', views.hundred),
    path('', views.home, name='home')
]
