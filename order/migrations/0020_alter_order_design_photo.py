# Generated by Django 4.1.5 on 2023-05-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_alter_order_design_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='design_photo',
            field=models.ImageField(blank=True, upload_to='photos/', verbose_name='Дизайн торта/ Фото'),
        ),
    ]
