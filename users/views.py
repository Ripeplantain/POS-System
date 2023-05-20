from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .decorators import authenticated_user
from .forms import UpdateUserForm, CreateUserForm


@login_required(login_url='login')
def register_view(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form .is_valid():
            form.save()
            messages.success(request, 'User has been added')
            return redirect('view_products')

    context = {
        'form':form
    }
    return render(request, 'users/add_user.html',context=context)

@login_required(login_url='login')
def profile_page(request):
    """
        This is for the profile page
    """
    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('view_products')

    context = {
        'form': form
    }
    return render(request, 'users/profile.html',context)


@authenticated_user
def login_view(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('view_products')
        else:
            messages.error(request, 'Invalid Credentials Given')
            return redirect('login')


    return render(request, 'users/login.html')


def logout_view(request):

    logout(request)
    return redirect('login')