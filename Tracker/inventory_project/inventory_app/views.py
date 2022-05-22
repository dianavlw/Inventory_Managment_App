import re
from django.shortcuts import render, redirect
from .models import Product, Warehouse, Shipment
from .forms import ProductForm, WarehouseForm , ShipmentForm
# Create your views here.


def shipments(request):
    all_shipments = Shipment.objects.all()
    return render(request, 'shipments.html', {'all_shipments': all_shipments})

def shipment_description(request, shipment_id):
    shipment = Shipment.objects.get(id=shipment_id)
    return render(request, 'shipment_description.html', {'shipment':shipment} ) 

def new_shipment(request):
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment=form.save(commit=False)
            shipment.save()
            return redirect('shipments')
        return render(request, 'shipments.html')
    else:
        form = ShipmentForm()
    return render(request, 'shipment_form.html', {'form': form, 'type': 'New'})

def shipment_edit(request, shipment_id):
    shipment = Shipment.objects.get(id=shipment_id)
    if request.method == "POST":
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
           shipment = form.save(commit=False)
           shipment.save()
           return redirect('shipment_description', shipment_id=shipment_id)
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipment_form.html', {'form': form, 'type': 'Edit'})


def delete_shipment(request, shipment_id):
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.delete()
        return redirect('shipments')






