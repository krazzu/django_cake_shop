from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_second_name', 'order_date', 'customer_tg',
                    'customer_phone_number', 'design_description', 'get_image', 'order_total', 'created']
    list_filter = ['customer_name', 'created', 'order_date']
    list_editable = ['order_total', 'order_date']

    def get_image(self, obj):
        if obj.design_photo:
            return mark_safe(f'<img src={obj.design_photo.url} width="100" height="100"/>')
        else:
            return None
    get_image.short_description = "Изображение"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
