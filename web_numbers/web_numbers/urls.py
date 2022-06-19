from django.contrib import admin
from django.urls import path
from orders.views import orders_page, inform_about_delay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', orders_page, name='home'),
    path('inform_about_delay', inform_about_delay, name='inform_about_delay')
]
