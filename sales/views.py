from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import SalesForm
from .models import SalesModel
from inventory.models import InventoryModel
# Create your views here.

def new_sale(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            sku = form.cleaned_data['sku']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            total_price = quantity * price

            not_available = False
            inventory = get_object_or_404(InventoryModel, sku=sku)
            if quantity <= inventory.available_quantity:
                model = SalesModel(customer=customer, sku=sku, quantity=quantity, price=price, total_price=total_price)
                model.save()

                inventory.available_quantity -= quantity
                inventory.save()
                return HttpResponseRedirect(reverse('sales-history'))
            else:
                not_available = True
                return render(request, 'sales/new_sale.html', {
                    'form': SalesForm,
                    'not_available': not_available
                })
    else:
        return render(request, 'sales/new_sale.html', {
            'form': SalesForm
        })


def sales_history(request):
    model = SalesModel.objects.all()
    return render(request, 'sales/sales_history.html', {
        'model': model
    })


def delete_sale(request, order_no):
    model = SalesModel.objects.get(order_no=order_no)
    model.delete()
    return HttpResponseRedirect(reverse('sales-history'))