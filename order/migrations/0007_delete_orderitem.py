# Generated by Django 4.1.5 on 2023-04-29 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_orderitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
