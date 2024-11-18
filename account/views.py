from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    # اگر کاربر وارد شده باشد، به صفحه داشبورد هدایت شود
    if request.user.is_authenticated:
        return redirect('order_list')

    # اگر درخواست POST باشد (یعنی فرم ارسال شده باشد)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # احراز هویت کاربر
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('order_list')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")

    return render(request, 'account/login.html')  # نمایش فرم لاگین
