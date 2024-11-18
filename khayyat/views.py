from django.shortcuts import render, redirect
from .models import Order
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def order_list(request):
    orders = Order.objects.all()


    return render(request, 'khayyat/index.html', {'orders': orders})



@login_required
def add_order(request):
    if request.method == 'POST':
        # گرفتن داده‌ها از فرم
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        fabric = request.POST.get('fabric')
        pants = request.POST.get('pants')
        shirt = request.POST.get('shirt')
        fabric_length = request.POST.get('fabric_length')
        date = request.POST.get('date')
        deposit = request.POST.get('deposit')
        wage = request.POST.get('wage')
        delivered = 'delivered' in request.POST  # برای چک‌باکس
        description = request.POST.get('description')

        # ذخیره اطلاعات در دیتابیس
        order = Order(
            fullname=fullname,
            phone=phone,
            fabric=fabric,
            pants=pants,
            shirt=shirt,
            fabric_length=fabric_length,
            date=date,
            deposit=deposit,
            wage=wage,
            delivered=delivered,
            description=description
        )
        order.save()

        # بعد از ذخیره، هدایت به صفحه لیست سفارشات
        return redirect('order_list')  # به آدرس لیست سفارشات هدایت می‌شود

    return render(request, 'khayyat/add-form.html')