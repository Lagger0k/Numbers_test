from django.db import models


class Order(models.Model):
    number = models.IntegerField('№')
    order_number = models.IntegerField('Заказ №')
    order_dollar_amount = models.DecimalField('Стоимость, $', max_digits=7, decimal_places=2)
    delivery_date = models.DateField('Срок поставки')
    order_rub_amount = models.DecimalField('Стоимость, Руб.', max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order_number = {self.order_number}"

    class Meta:
        db_table = 'orders'
