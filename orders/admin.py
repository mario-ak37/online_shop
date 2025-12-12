from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        "created",
        "updated",
    ]

    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
