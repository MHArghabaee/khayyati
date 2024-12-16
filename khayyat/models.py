from django.db import models


class Order(models.Model):
    # اطلاعات مشتری
    fullname = models.CharField(max_length=100, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="شماره تلفن")

    # مشخصات شلوار
    pants_fabric = models.CharField(max_length=200, null=True, blank=True, verbose_name="پارچه شلوار")
    pants_fabric_length = models.CharField(max_length=100, null=True, blank=True, verbose_name="متراژ پارچه شلوار")
    pants_length = models.CharField(max_length=50, null=True, blank=True, verbose_name="قد شلوار")
    pants_waist = models.CharField(max_length=50, null=True, blank=True, verbose_name="کمر شلوار")
    pants_thigh = models.CharField(max_length=50, null=True, blank=True, verbose_name="ران شلوار")
    pants_knee = models.CharField(max_length=50, null=True, blank=True, verbose_name="زانو شلوار")
    pants_hem = models.CharField(max_length=50, null=True, blank=True, verbose_name="دمپای شلوار")
    pants_crotch = models.CharField(max_length=50, null=True, blank=True, verbose_name="فاق شلوار")

    # مشخصات پیراهن
    shirt_fabric = models.CharField(max_length=200, null=True, blank=True, verbose_name="پارچه پیراهن")
    shirt_fabric_length = models.CharField(max_length=100, null=True, blank=True, verbose_name="متراژ پارچه پیراهن")
    shirt_length = models.CharField(max_length=50, null=True, blank=True, verbose_name="قد پیراهن")
    shirt_shoulder = models.CharField(max_length=50, null=True, blank=True, verbose_name="سرشانه پیراهن")
    shirt_collar = models.CharField(max_length=50, null=True, blank=True, verbose_name="یقه پیراهن")
    shirt_armpit = models.CharField(max_length=50, null=True, blank=True, verbose_name="زیر بغل پیراهن")
    shirt_sleeve = models.CharField(max_length=50, null=True, blank=True, verbose_name="آستین پیراهن")
    shirt_details = models.TextField(null=True, blank=True, verbose_name="جزئیات پیراهن")

    # اطلاعات کلی سفارش
    entry_date = models.CharField(max_length=120, blank=True, null=True, verbose_name="تاریخ ورود")
    delivery_date = models.CharField(max_length=120, blank=True, null=True, verbose_name="تاریخ تحویل")
    deposit = models.CharField(max_length=120, blank=True, null=True, verbose_name="بیعانه (تومان)")
    wage = models.CharField(max_length=120, blank=True, null=True, verbose_name="اجرت (تومان)")
    delivered = models.BooleanField(default=False, verbose_name="آیا تحویل داده شده است؟")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return f"{self.fullname} | تحویل داده شده: {'بله' if self.delivered else 'خیر'}"

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"
