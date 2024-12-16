from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'khayyat/index.html', {'orders': orders})


@login_required
def add_order(request):
    if request.method == 'POST':
        # گرفتن داده‌ها از فرم
        order = Order(
            fullname=request.POST.get('fullname'),
            phone=request.POST.get('phone'),
            pants_fabric=request.POST.get('pants_fabric'),
            pants_fabric_length=request.POST.get('pants_fabric_length'),
            pants_length=request.POST.get('pants_length'),
            pants_waist=request.POST.get('pants_waist'),
            pants_thigh=request.POST.get('pants_thigh'),
            pants_knee=request.POST.get('pants_knee'),
            pants_hem=request.POST.get('pants_hem'),
            pants_crotch=request.POST.get('pants_crotch'),
            shirt_fabric=request.POST.get('shirt_fabric'),
            shirt_fabric_length=request.POST.get('shirt_fabric_length'),
            shirt_length=request.POST.get('shirt_length'),
            shirt_shoulder=request.POST.get('shirt_shoulder'),
            shirt_collar=request.POST.get('shirt_collar'),
            shirt_armpit=request.POST.get('shirt_armpit'),
            shirt_sleeve=request.POST.get('shirt_sleeve'),
            shirt_details=request.POST.get('shirt_details'),
            entry_date=request.POST.get('entry_date'),
            delivery_date=request.POST.get('delivery_date'),
            deposit=request.POST.get('deposit'),
            wage=request.POST.get('wage'),
            delivered='delivered' in request.POST,  # چک‌باکس
            description=request.POST.get('description'),
        )
        order.save()

        # بعد از ذخیره، هدایت به صفحه لیست سفارشات
        return redirect('order_list')

    return render(request, 'khayyat/add-form.html')


@login_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # گرفتن داده‌ها از فرم
        order.fullname = request.POST.get('fullname')
        order.phone = request.POST.get('phone')
        order.pants_fabric = request.POST.get('pants_fabric')
        order.pants_fabric_length = request.POST.get('pants_fabric_length')
        order.pants_length = request.POST.get('pants_length')
        order.pants_waist = request.POST.get('pants_waist')
        order.pants_thigh = request.POST.get('pants_thigh')
        order.pants_knee = request.POST.get('pants_knee')
        order.pants_hem = request.POST.get('pants_hem')
        order.pants_crotch = request.POST.get('pants_crotch')
        order.shirt_fabric = request.POST.get('shirt_fabric')
        order.shirt_fabric_length = request.POST.get('shirt_fabric_length')
        order.shirt_length = request.POST.get('shirt_length')
        order.shirt_shoulder = request.POST.get('shirt_shoulder')
        order.shirt_collar = request.POST.get('shirt_collar')
        order.shirt_armpit = request.POST.get('shirt_armpit')
        order.shirt_sleeve = request.POST.get('shirt_sleeve')
        order.shirt_details = request.POST.get('shirt_details')
        order.entry_date = request.POST.get('entry_date')
        order.delivery_date = request.POST.get('delivery_date')
        order.deposit = request.POST.get('deposit')
        order.wage = request.POST.get('wage')
        order.delivered = 'delivered' in request.POST
        order.description = request.POST.get('description')

        # ذخیره تغییرات
        order.save()

        # هدایت به صفحه لیست سفارشات
        return redirect('order_list')

    return render(request, 'khayyat/update.html', {'order': order})


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_list')
