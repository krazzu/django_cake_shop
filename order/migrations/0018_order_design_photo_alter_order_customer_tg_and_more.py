# Generated by Django 4.1.5 on 2023-05-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_remove_order_customer_email_order_customer_tg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='design_photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Дизайн торта/ Фото'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_tg',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='order',
            name='design_description',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='Дизайн торта'),
        ),
    ]