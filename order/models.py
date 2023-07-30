from django.db import models
from my_shop.models import Product


class Order(models.Model):
    order_date = models.DateTimeField('Число закаказа')
    customer_name = models.CharField('Имя', max_length=150, db_index=True)
    customer_second_name = models.CharField('Фамилия', max_length=150, db_index=True)
    customer_tg = models.CharField('Телеграм', max_length=256, default="", blank=True)
    customer_phone_number = models.CharField('Номер телефона', max_length=12)
    design_description = models.TextField('Дизайн торта', max_length=1000, default="", blank=True)
    design_photo = models.ImageField('Дизайн торта/ Фото', blank=True, upload_to='photos/')
    order_total = models.DecimalField('Итоговая стоимость', max_digits=10, decimal_places=2)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ('customer_name',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.customer_name


class OrderItem(models.Model):
    order = models.CharField('Номер заказа', max_length=251)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return self.product.name