from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
from .forms import OrderForm, DepartmentForm
from .models import Departments, Order
from products.models import Product
from .utils import generate_random_string


@login_required(login_url='login')
def add_departments(request):

    form = DepartmentForm()

    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully')
            return redirect('view_products')

    context = {
        'form':form
    }
    return render(request, 'orders/add_department.html', context=context)


@login_required(login_url='login')
def view_orders(request):
    """ A view to return the orders page """

    orders = Order.objects.all().order_by('-created_at')
    departments = Departments.objects.all()

    if request.method == 'POST':
        search = request.POST['search']
        if search == "all":
            orders = Order.objects.all().order_by('-created_at')
        else:
            orders = Order.objects.filter(
                                    Q(user__first_name__icontains=search) |
                                    Q(user__last_name__icontains=search) |
                                    Q(department__name__icontains=search) |
                                    Q(order_number__icontains=search) |
                                    Q(product__name__icontains=search)
            ).order_by('-created_at')

    page = Paginator(orders, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    context = {
        'page': page,
        'departments': departments,
    }

    return render(request, 'orders/view_orders.html', context=context)




@login_required(login_url='login')
def add_order(request,id):
    """ A view to return the add order page """

    form = OrderForm()
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST)# Example usage
        if form.is_valid():
            if product.quantity >= form.cleaned_data["quantity"]:
                product.quantity -= form.cleaned_data["quantity"]
                product.save()
                product_order = form.save(commit=False)
                product_order.user = request.user
                product_order.order_number = generate_random_string()
                product_order.save()
                messages.success(request, 'Order has been created successfully')
                return redirect('view_products')
            else:
                messages.error(request, 'order quantity is greater than what we have in stock')
                return redirect('view_products')
        else:
            messages.error(request, 'Failed to add order. Please ensure the form is valid.')
    

    context = {
        'form': form
    }
    return render(request, 'orders/add_order.html', context)



@login_required(login_url='login')
def delete_order(request,id):

    order = get_object_or_404(Order,id=id)
    product = get_object_or_404(Product,id=order.product.id)

    product.quantity += order.quantity
    product.save()
    order.delete()
    messages.success(request, 'Order has been deleted successfully')

    return redirect('view_orders')