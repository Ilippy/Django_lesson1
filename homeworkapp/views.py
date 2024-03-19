from django.db.models import F, Sum
from django.shortcuts import render
from .models import OrderProduct, Product
from django.utils import timezone
from django.views.generic.edit import CreateView
from .forms import ProductForm
# from django.views.generic import ListView, DetailView


# Homework 1
# from django.template.loader import render_to_string
# from django.http import HttpResponse
# def v1(request):
#     with open('homeworkapp/templates/homeworkapp/hw.html', 'r', encoding='utf-8') as file:
#         result = file.read()
#     return HttpResponse(result)
#
#
# def v2(request):
#     result = render_to_string('homeworkapp/hw.html')
#     return HttpResponse(result)
#
#
# def v3(request):
#     render(request, 'homeworkapp/hw.html')

# Homework3
def get_orders_by_amount_of_days(request, days, user_id):
    date = timezone.now() - timezone.timedelta(days=days)
    result = OrderProduct.objects.prefetch_related('order', 'product').filter(
        order__created_at__gt=date, order__customer=user_id
    ).values(
        name=F('product__name')
    ).annotate(
        count=Sum('order_amount')
    )
    context = {
        'days': days,
        'products': result,
    }

    return render(request, 'homeworkapp/products_by_date.html', context)


# Homework 4
class ProductsListCreateView(CreateView):
    model = Product
    template_name = 'homeworkapp/products.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.model.objects.all()
        return context
