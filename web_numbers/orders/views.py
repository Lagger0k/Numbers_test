from django.shortcuts import render, redirect
from django.db.models import Sum

from orders.models import Order
from orders.services.service import get_order_models_from_db


def orders_page(request):
    orders = get_order_models_from_db()
    dollar_sum = Order.objects.all().aggregate(Sum('order_dollar_amount'))
    ruble_sum = Order.objects.all().aggregate(Sum('order_rub_amount'))
    return render(request,
                  'orders_page.html',
                  {
                      'orders': orders,
                      'dollar_sum': dollar_sum,
                      'ruble_sum': ruble_sum
                  }
                  )


def inform_about_delay(request):
    if request.method == 'POST':
        # здесь должна быть логика уведомлений через телеграм, для этого у нас должен быть запущен контейнер с ботом,
        # который при старте юзером, сохраняет его user_id в модель users и потом использует его для отправки сообщений
        return redirect('home')
