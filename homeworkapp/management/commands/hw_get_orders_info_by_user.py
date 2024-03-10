from homeworkapp.models import User, OrderProduct
from django.core.management.base import BaseCommand


# from django.db import connection


class Command(BaseCommand):
    help = "Read all orders' info by user ID"

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID')

    def handle(self, *args, **options):
        user = User.objects.get(pk=options['user_id'])

        query = OrderProduct.objects.select_related(
            'product', 'order'
        ).filter(order__customer=user).values(
            'order__id', 'product__name', 'product__price', 'order_amount'
        )
        self.stdout.write(f"All orders' info by user {user.name}")
        self.stdout.write("{:<10}{:<30}{:<10}{:<8}".format(
            'Order id', 'Product Name', 'Price', 'Amount', ))
        for product in query:
            info = f"{product['order__id']:<10}{product['product__name']:<30}" \
                   f"{product['product__price']:<10}{product['order_amount']:<8}"
            self.stdout.write(info)

        # print(query)
        # print(*connection.queries, len(connection.queries), sep='\n')
