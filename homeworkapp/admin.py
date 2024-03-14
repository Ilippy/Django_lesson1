from django.contrib import admin
from .models import Order, User, OrderProduct, Product


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    list_editable = ['email', 'phone_number']
    # list_filter = ['name']


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    list_display = ['id', 'customer', 'total_price', 'created_at']
    list_editable = ['customer', 'total_price']
    # list_filter = ['customer', 'total_price']
    # filter_horizontal = ['products']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    list_display = ['id', 'name', 'price', 'amount']
    list_editable = ['name', 'price', 'amount']
    search_fields = ['name', 'price']




