# Generated by Django 4.1.5 on 2023-04-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_email',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_tg',
            field=models.CharField(default='', max_length=256, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='order',
            name='design_description',
            field=models.TextField(default='', max_length=1000, verbose_name='Дизайн торта'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.CharField(max_length=251, verbose_name='Номер заказа'),
        ),
    ]