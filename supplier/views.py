from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import SupplierForm, SupplierEditForm
from .models import SupplierModel

# Create your views here.

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            model = SupplierModel(name=name, contact=contact,
                                  email=email, address=address)
            model.save()
            return HttpResponseRedirect(reverse('suppliers-list'))
    else:
        return render(request, 'supplier/add_supplier.html', {
            'form': SupplierForm
        })


def suppliers_list(request):
    suppliers = SupplierModel.objects.all()
    return render(request, 'supplier/suppliers_list.html', {
        'suppliers': suppliers
    })


def edit_supplier(request, name):
    model = SupplierModel.objects.get(name=name)
    if request.method == 'POST':
        form = SupplierEditForm(request.POST)
        if form.is_valid():
            model.contact = form.cleaned_data['contact']
            model.email = form.cleaned_data['email']
            model.address = form.cleaned_data['address']
            model.save(update_fields=['contact', 'email', 'address'])
            return HttpResponseRedirect(reverse('suppliers-list'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('suppliers-list'))
    else:
        initial = {
            'contact': model.contact,
            'email': model.email,
            'address': model.address,
        }
        form = SupplierEditForm(initial=initial)
        return render(request, 'supplier/add_supplier.html', {
            'form': form,
            'name': name
        })

def delete_supplier(request, name):
    model = SupplierModel.objects.get(name=name)
    model.delete()
    return HttpResponseRedirect(reverse('suppliers-list'))