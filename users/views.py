from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
def register_customer(request):
    if request.POST:
        form = ResgisterCustomerForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.is_customer = True
            new.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid username or password')   
            return redirect('register')  
    else:
        form = ResgisterCustomerForm()
    return render(request, 'register.html', {'form': form})

def login_customer(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_customer(request):
    logout(request)
    messages.warning(request, 'Logged out successfully')
    return redirect('login')