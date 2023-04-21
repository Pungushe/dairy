from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

from .models import (
    Product,
    Customer,
    Cart,
    Payment,
    OrderPlace,
    Wishlist
)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount_price', 'category', 'product_image']


@admin.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

    def products(self, obj):
        link = reverse('admin:shop_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_order_status', 'razorpay_payment_id', 'paid']


@admin.register(OrderPlace)
class OrderPlaceModelAdmit(admin.ModelAdmin):
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'order_date', 'status', 'payments']

    def customers(self, obj):
        link = reverse('admin:shop_customer_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.name)

    def products(self, obj):
        link = reverse('admin:shop_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def payments(self, obj):
        link = reverse('admin:shop_payment_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)


@admin.register(Wishlist)
class WishlistModelAdmit(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']

    def products(self, obj):
        link = reverse('admin:shop_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


# admin.site.unregister(Group)
