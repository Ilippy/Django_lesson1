from django.urls import path
from . import views

urlpatterns = [
    # path('v1/', views.v1),
    # path('v2/', views.v2),
    # path('v3/', views.v3),
    path('user/<int:user_id>/orders_for_last/<int:days>/', views.get_orders_by_amount_of_days),
    path('products/', views.ProductsListCreateView.as_view(), name='products')
]
