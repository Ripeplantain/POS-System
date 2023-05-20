from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



# Create your views here.
from .models import Product
from orders.models import Departments
from .forms import ProductForm

from django.http import HttpResponse

@login_required(login_url='login')
def view_products(request):

    products = Product.objects.all().order_by('-created_at')

    if request.method == 'POST':
        search = request.POST['search']
        products = Product.objects.filter(name__icontains=search).order_by('-created_at')

    page = Paginator(products, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    context = {
        'page': page,
        'count': products.count(),
        'department_count':Departments.objects.all().count()
    }

    return render(request, 'products/view_products.html', context=context)



@login_required(login_url='login')
def add_product(request):

    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('view_products')
        else:
            messages.error(request, 'Error adding product')
            return redirect('add_product')
        
    context = {
        'form': form
    }

    return render(request, 'products/add_product.html', context=context)


@login_required(login_url='login')
def update_product(request,id):

    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('view_products')
        else:
            messages.error(request, 'Error updating product')
            return redirect('update_product')
        
    context = {
        'form':form
    }
    return render(request, 'products/add_product.html', context=context)



@login_required(login_url='login')
def delete_product(request,id):

    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, 'Product has been deleted successful')
    return redirect('view_products')