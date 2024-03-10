from homeworkapp.models import Order, OrderProduct, Product, User
from django.db import connection
from django.db.models import Sum, F


def run():
    order = Order.objects.first()
    # result = 0
    # .select_related('product')
    # .prefetch_related('order', 'product')
    query = OrderProduct.objects.filter(order=order).annotate(
        sub_total=F('order_amount') * F('product__price')
    ).aggregate(result=Sum('sub_total'))

    # for op in ops:
    #     result += op.product.price * op.order_amount
    # for op in ops:
    #     result += op['order_amount'] * op['product__price']

    result = round(query['result'], 2)
    print(result, type(result))
    # print(result)
    print(*connection.queries, len(connection.queries), sep='\n')
