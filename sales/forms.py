from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import SalesModel


class SalesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.form_action = ''
            self.helper.add_input(Submit('submit', 'Save', css_class='mt-2 btn btn-dark'))
            self.helper.add_input(Button('cancel', 'Cancel', onclick="location.href = '/sales/sales-history/'", css_class='ms-3 mt-2 btn btn-dark'))
            self.helper.layout = Layout(
                Row(
                    Column('customer', css_class='mt-4'),
                    Column('sku', css_class='mt-4'),
                    Column('quantity', css_class='mt-4'),
                    Column('price', css_class='mt-4'),
                )
            )

    class Meta:
        model = SalesModel
        exclude = ['order_no', 'date', 'total_price']
        labels = {
            'customer': 'Customer Name',
            'sku': 'SKU',
            'quantity': 'Quantity',
            'price': 'Price Per Quantity (Rs.)'
            }
