from django.db import models


class Order(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن")
    fabric = models.CharField(max_length=200, verbose_name="مشخصات پارچه")
    pants = models.CharField(max_length=200, verbose_name="مشخصات شلوار")
    shirt = models.CharField(max_length=200, verbose_name="مشخصات پیراهن")
    fabric_length = models.CharField(max_length=100, null=True, blank=True, verbose_name="متراژ")
    date = models.CharField(max_length=10, verbose_name="تاریخ تحویل")
    deposit = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="بیعانه(تومان)")
    wage = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="اجرت(تومان)")
    delivered = models.BooleanField(default=False, verbose_name="تحویل")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return f"{self.fullname}   |   {self.delivered}"

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"
