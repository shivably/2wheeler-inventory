from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import NewStockModel


class NewStockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.form_action = ''
            self.helper.add_input(Submit('submit', 'Save', css_class='mt-2 btn btn-dark'))
            self.helper.add_input(Button('cancel', 'Cancel', onclick="location.href = '/purchase/purchase-history/'", css_class='ms-3 mt-2 btn btn-dark'))
            self.helper.layout = Layout(
                Row(
                    Column('sku', css_class='mt-4'),
                    Column('supplier', css_class='mt-4'),
                    Column('number', css_class='mt-4'),
                    Column('chassis_number', css_class='mt-4'),
                    Column('engine_number', css_class='mt-4'),
                    Column('registration_date', css_class='mt-4'),
                    Column('manufacturing_date', css_class='mt-4'),
                    Column('purchase_price', css_class='mt-4'),
                    Column('noc', css_class='mt-4'),
                    Column('noc_date', css_class='mt-4'),
                )
            )

    class Meta:
        model = NewStockModel
        exclude = ['order_no', 'date', 'sale_price', 'quantity']
        labels = {
            'sku': 'SKU',
            'supplier': 'Supplier',
            'number': 'Reg.No',
            'chassis_number': 'Ch.No',
            'engine_number': 'Eng.No',
            'registration_date': 'Registration',
            'manufacturing_date': 'Manufacturing',
            'purchase_price': 'Price',
            'noc': 'NOC',
            'noc_date': 'NOC Date' 
        }
