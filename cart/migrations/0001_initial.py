# Generated by Django 4.1.5 on 2023-04-29 06:05

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
                ('order_date', models.DateTimeField(verbose_name='Число закаказа')),
                ('customer_name', models.CharField(db_index=True, max_length=150, verbose_name='Имя')),
                ('customer_second_name', models.CharField(db_index=True, max_length=150, verbose_name='Фамилия')),
                ('customer_email', models.EmailField(default='', max_length=256, verbose_name='Почта')),
                ('customer_phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая стоимость')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('customer_name',),
            },
        ),
    ]