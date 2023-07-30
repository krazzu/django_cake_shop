from django import forms

QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CartAddProductForm(forms.Form):
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-control'}), label="Количество")
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
