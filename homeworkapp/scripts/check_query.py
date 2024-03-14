from homeworkapp.models import Order, OrderProduct, Product, User
from django.db import connection
from django.db.models import Sum, F
from django.utils import timezone
from pprint import pprint


# from faker import Faker
#
# fake = Faker('ru_RU')


def run():
    # order = Order.objects.first()
    # result = 0
    # .select_related('product')
    # .prefetch_related('order', 'product')
    # query = OrderProduct.objects.filter(order=order).annotate(
    #     sub_total=F('order_amount') * F('product__price')
    # ).aggregate(result=Sum('sub_total'))

    days = 180
    date = timezone.now() - timezone.timedelta(days=days)
    # result = Product.objects.prefetch_related('order').filter(
    #     orders__created_at__gt=date
    # ).aggregate(
    #     res=Sum('orderproduct__order_amount')
    # ).values(
    #     'name', 'res'
    # )
    result = OrderProduct.objects.prefetch_related('order', 'product').filter(
        order__created_at__gt=date
    ).values(
        name=F('product__name')
    ).annotate(
        count=Sum('order_amount')
    )

    # result = round(query['result'], 2)
    # print(result, type(result))
    print(result)
    pprint(connection.queries)
