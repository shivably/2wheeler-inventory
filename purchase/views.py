from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import NewStockForm
from .models import NewStockModel
from inventory.models import InventoryModel
# Create your views here.


@login_required
def purchase_stock(request):
    if request.method == 'POST':
        form = NewStockForm(request.POST)
        if form.is_valid():
            sku = form.cleaned_data['sku']
            supplier = form.cleaned_data['supplier']
            number = form.cleaned_data['number']
            chassis_number = form.cleaned_data['chassis_number']
            engine_number = form.cleaned_data['engine_number']
            registration_date = form.cleaned_data['registration_date']
            manufacturing_date = form.cleaned_data['manufacturing_date']
            purchase_price = form.cleaned_data['purchase_price']
            sale_price = round(purchase_price + (purchase_price * 0.20), 2) 

            model = NewStockModel(sku=sku, supplier=supplier, number=number, 
                                  chassis_number=chassis_number, engine_number=engine_number,
                                  registration_date=registration_date, manufacturing_date=manufacturing_date,
                                  purchase_price=purchase_price, sale_price=sale_price)
            model.save()

            inventory = get_object_or_404(InventoryModel, name=sku)
            inventory.available_quantity += 1
            inventory.save()
            return HttpResponseRedirect(reverse('purchase-history'))
    else:
        return render(request, 'purchase/purchase_stock.html', {
            'form': NewStockForm
        })


@login_required
def purchase_history(request):
    purchases = NewStockModel.objects.all()
    return render(request, 'purchase/purchase_history.html', {
        'purchases': purchases
    })


@login_required
def delete_purchase(request, order_no):
    stock = NewStockModel.objects.get(order_no=order_no)
    stock.delete()
    inventory = get_object_or_404(InventoryModel, name=stock.sku)
    inventory.available_quantity -= 1
    inventory.save()
    return HttpResponseRedirect(reverse('purchase-history'))


@login_required
def edit_purchase(request, order_no):
    model = NewStockModel.objects.get(order_no=order_no)
    if request.method == 'POST':
        form = NewStockForm(request.POST)
        if form.is_valid():
            model.sku = form.cleaned_data['sku']
            model.supplier = form.cleaned_data['supplier']
            model.number = form.cleaned_data['number']
            model.chassis_number = form.cleaned_data['chassis_number']
            model.engine_number = form.cleaned_data['engine_number']
            model.registration_date = form.cleaned_data['registration_date']
            model.manufacturing_date = form.cleaned_data['manufacturing_date']
            model.purchase_price = form.cleaned_data['purchase_price']
            model.sale_price = round(model.purchase_price + (model.purchase_price * 0.20), 2) 
            model.save(update_fields=['sku', 'supplier', 'purchase_price', 'noc', 'noc_date'])
            return HttpResponseRedirect(reverse('purchase-history'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('purchase-history'))
    else:
        initial = {
            'order_no': model.order_no,
            'sku': model.sku,
            'supplier': model.supplier,
            'number': model.number,
            'chassis_number': model.chassis_number,
            'engine_number': model.engine_number,
            'registration_date': model.registration_date,
            'manufacturing_date': model.manufacturing_date,
            'purchase_price': model.purchase_price,
            'noc': model.noc,
            'noc_date': model.noc_date
        }
        form = NewStockForm(initial=initial)
        return render(request, 'supplier/add_supplier.html', {
            'form': form,
            'order_no': order_no
        })