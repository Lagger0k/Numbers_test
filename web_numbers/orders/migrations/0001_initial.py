# Generated by Django 4.0.5 on 2022-06-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='№')),
                ('order_number', models.IntegerField(verbose_name='Заказ №')),
                ('order_dollar_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость, $')),
                ('delivery_date', models.DateField(verbose_name='Срок поставки')),
                ('order_rub_amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость, Руб.')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
