from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    # اگر کاربر وارد شده باشد، به صفحه داشبورد هدایت شود
    if request.user.is_authenticated:
        return redirect('order_list')  # یا هر صفحه‌ای که می‌خواهید به آن هدایت کنید

    # اگر درخواست POST باشد (یعنی فرم ارسال شده باشد)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # احراز هویت کاربر
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "ورود موفقیت‌آمیز بود!")
            return redirect('order_list')  # هدایت به لیست
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")

    return render(request, 'account/login.html')  # نمایش فرم لاگین
