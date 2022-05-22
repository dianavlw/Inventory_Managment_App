from django.shortcuts import render, redirect
from .models import Product, Warehouse
from .forms import ProductForm, WarehouseForm 


def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'all_products': all_products,})

def product_description(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_description.html', {'product': product})

def new_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_description', product_id=product.id)
    else:
        form = ProductForm() 
    return render(request, 'product_form.html', {'form': form, 'type': 'New'})


def product_edit(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product= form.save(commit=False)
            product.save()
            return redirect('product_description', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'type': 'Edit'})

def product_delete(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.delete()
    return redirect('products')




# warehouse
def warehouse_description(request, product_id, warehouse_id):
    product = Product.objects.get(id=product_id)
    warehouse = Warehouse.objects.get(id=warehouse_id)
    return render(request, 'warehouse_description.html', {'product': product, 'warehouse': warehouse})

def new_warehouse(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse= form.save(commit=False)
            warehouse.save()
            return redirect('warehouse_description', product_id=product.id, warehouse_id=warehouse.id)
    else:
        form = WarehouseForm(initial={'product': product})
    return render(request, 'warehouse_form.html', {'form': form, 'type': 'New', 'product': product})

def edit_warehouse(request, product_id, warehouse_id):
    product = Product.objects.get(id=product_id)
    warehouse = Warehouse.objects.get(id=warehouse_id)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.save()
            return redirect('warehouse_description', product_id=product.id, warehouse_id=warehouse.id)
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouse_form.html', {'form': form, 'type': 'Edit', 'product': product})

def delete_warehouse(request, product_id, warehouse_id):
    if request.method == 'POST':
        warehouse = Warehouse.objects.get(id=warehouse_id)
        warehouse.delete()
    return redirect('product_description', product_id=product_id)

