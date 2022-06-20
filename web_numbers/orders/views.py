from django.shortcuts import render, redirect
from django.db.models import Sum

from orders.models import Order
from orders.services.bot_mailing import send_message
from orders.services.service import get_order_models_from_db, get_delay_orders


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
        delay_orders = get_delay_orders()
        text = 'Заказы:\n' + ' \n'.join(delay_orders) + '\n' 'опаздывают'
        send_message(text)
        return redirect('home')
