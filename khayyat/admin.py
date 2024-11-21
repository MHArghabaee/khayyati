from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'fabric', 'pants', 'shirt', 'fabric_length', 'date', 'deposit', 'wage', 'delivered')
    list_filter = ('delivered',)
    search_fields = ('fullname', 'phone', 'fabric', 'pants', 'shirt', 'date')
    ordering = ('-date',)
