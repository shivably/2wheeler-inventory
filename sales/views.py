from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import SalesFormset, SalesFormHelper, CustomerForm
from .models import SalesModel, CustomerModel, NewStockModel
from inventory.models import InventoryModel
# Create your views here.

@login_required
def new_sale(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        formset = SalesFormset(request.POST)
        formhelper = SalesFormHelper()

        invalid_request = False
        if customer_form.is_valid() and formset.is_valid():
            customer = customer_form.cleaned_data['customer']
            contact = customer_form.cleaned_data['contact']
            for form in formset:
                stock = form.cleaned_data['stock']
                advance = form.cleaned_data['advance']
                deal_price = form.cleaned_data['deal_price']
                
                not_available = False
                if not stock.sold:
                    cust_model = CustomerModel(customer=customer, contact=contact)
                    cust_model.save()
                    
                    model = SalesModel(customer=cust_model, stock=stock, advance=advance, deal_price=deal_price, final_price=deal_price)
                    model.save()

                    stock.sold = True
                    stock.save()

                    inventory = stock.sku
                    inventory.available_quantity -= 1
                    inventory.save()
                else:
                    not_available = True
                    return render(request, 'sales/new_sale.html', {
                        'customer_form': CustomerForm(),
                        'formset': SalesFormset(queryset=SalesModel.objects.none()),
                        'helper': formhelper,
                        'not_available': not_available
                    })
            return HttpResponseRedirect(reverse('sales-history'))
        else:
            invalid_request = True
            return render(request, 'sales/new_sale.html', {
                'invalid_request': invalid_request,
                'customer_form': CustomerForm(),
                'formset': SalesFormset(queryset=SalesModel.objects.none()),
                'helper': SalesFormHelper()
            })

    else:
        return render(request, 'sales/new_sale.html', {
            'customer_form': CustomerForm(),
            'formset': SalesFormset(queryset=SalesModel.objects.none()),
            'helper': SalesFormHelper()
        })


@login_required
def sales_history(request):
    model = SalesModel.objects.all()
    return render(request, 'sales/sales_history.html', {
        'model': model
    })


@login_required
def delete_sale(request, order_no):
    model = SalesModel.objects.get(order_no=order_no)
    model.delete()
    return HttpResponseRedirect(reverse('sales-history'))