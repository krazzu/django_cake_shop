# Generated by Django 4.1.5 on 2023-04-22 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options_order_uploaded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='uploaded',
        ),
    ]
