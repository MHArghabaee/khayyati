from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    # مشخصات نمایش داده شده در لیست
    list_display = (
        'fullname', 'phone', 'pants_fabric', 'pants_fabric_length', 'pants_length',
        'pants_waist', 'pants_thigh', 'pants_knee', 'pants_hem', 'pants_crotch',
        'shirt_fabric', 'shirt_fabric_length', 'shirt_length', 'shirt_shoulder',
        'shirt_collar', 'shirt_armpit', 'shirt_sleeve', 'shirt_details', 'entry_date',
        'delivery_date', 'deposit', 'wage', 'delivered'
    )

    # قابل جستجو
    search_fields = ('fullname', 'phone', 'shirt_fabric', 'pants_fabric')

    # قابلیت فیلترها
    list_filter = (
        'delivered', 'entry_date', 'delivery_date',
    )

    # فیلدهای قابل ویرایش
    list_editable = ('delivered',)

    # امکان مرتب‌سازی
    ordering = ('entry_date',)

    # نمای عمومی (چگونه داده‌ها در پانل ادمین نمایش داده شوند)
    readonly_fields = ('entry_date', 'delivery_date', 'deposit', 'wage', 'description')

    # فیلتر بالا
    filter_horizontal = ()

    # فرم ویرایش
    fieldsets = (
        (None, {
            'fields': (
                'fullname', 'phone',
                ('pants_fabric', 'pants_fabric_length', 'pants_length',
                 'pants_waist', 'pants_thigh', 'pants_knee', 'pants_hem', 'pants_crotch'),
                ('shirt_fabric', 'shirt_fabric_length', 'shirt_length',
                 'shirt_shoulder', 'shirt_collar', 'shirt_armpit', 'shirt_sleeve', 'shirt_details'),
                ('entry_date', 'delivery_date', 'deposit', 'wage', 'delivered', 'description'),
            )
        }),
    )


# ثبت پنل ادمین
admin.site.register(Order, OrderAdmin)
