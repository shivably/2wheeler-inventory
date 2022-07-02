from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import NewStockForm
from .models import NewStockModel
# Create your views here.


def purchase_stock(request):
    if request.method == 'POST':
        form = NewStockForm(request.POST)
        if form.is_valid():
            sku = form.cleaned_data['sku']
            supplier = form.cleaned_data['supplier']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            if NewStockModel.objects.filter(sku=sku):
                return render(request, 'purchase/purchase_stock.html', {
                    'form': NewStockForm,
                    'sku_present': True
                })
            else:
                model = NewStockModel(
                    sku=sku, supplier=supplier, quantity=quantity, price=price)
                model.save()
                return HttpResponseRedirect(reverse('purchase-history'))
    else:
        return render(request, 'purchase/purchase_stock.html', {
            'form': NewStockForm
        })


def purchase_history(request):
    purchases = NewStockModel.objects.all()
    return render(request, 'purchase/purchase_history.html', {
        'purchases': purchases
    })


def edit_purchase(request, sku):
    model = NewStockModel.objects.get(sku=sku)
    if request.method == 'POST':
        form = NewStockForm(request.POST)
        if form.is_valid():
            model.sku = form.cleaned_data['sku']
            model.supplier = form.cleaned_data['supplier']
            model.quantity = form.cleaned_data['quantity']
            model.price = form.cleaned_data['price']
            model.save(update_fields=['sku', 'supplier', 'quantity', 'price'])
            return HttpResponseRedirect(reverse('purchase-history'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('purchase-history'))
    else:
        initial = {
            'sku': model.sku,
            'supplier': model.supplier,
            'quantity': model.quantity,
            'price': model.price
        }
        form = NewStockForm(initial=initial)
        return render(request, 'purchase/purchase_stock.html', {
            'form': form,
            'sku': sku
        })


def delete_purchase(request, sku):
    model = NewStockModel.objects.get(sku=sku)
    model.delete()
    return HttpResponseRedirect(reverse('purchase-history'))
