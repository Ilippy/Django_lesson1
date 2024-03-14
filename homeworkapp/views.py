from django.db.models import F, Sum
from django.shortcuts import render
from .models import OrderProduct
from django.utils import timezone


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
def get_orders_by_amount_of_days(request, days):
    timezone.now()
    date = timezone.now() - timezone.timedelta(days=days)
    result = OrderProduct.objects.prefetch_related('order', 'product').filter(
        order__created_at__gt=date  # , order__customer=user_id
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
