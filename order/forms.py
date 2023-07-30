from django import forms
from django.utils import timezone
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'customer_name', 'customer_second_name', 'customer_tg', 'design_description',
                  'design_photo', 'customer_phone_number']
        widgets = {
            'order_date': forms.DateTimeInput(attrs={'class': 'form-control',
                                                     'min': timezone.now().strftime('%Y-%m-%dT%H:%M'),
                                                     'type': 'date'}),
            'customer_tg': forms.TextInput(attrs={'class': 'form-control'}),
            'design_description': forms.Textarea(attrs={'class': 'form-control', 'cols': "24", 'rows': "5"}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'customer_name': 'Имя',
            'customer_second_name': 'Фамилия',
            'customer_phone_number': 'Телефон',
        }

    def clean_order_date(self):
        order_date = self.cleaned_data.get('order_date')
        if order_date < timezone.now():
            raise forms.ValidationError('Дата заказа должна быть больше или равна текущей дате.')
        return order_date
