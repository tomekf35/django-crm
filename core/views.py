from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages


def homepage_view(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect('login')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfull') 
            return redirect('homepage')
        else:
            messages.success(request, 'Wrong username or password') 
            return render(request, 'login.html')
    else:
        return render(request, 'login.html', {'form': form})
    
    
def logout_view(request):
    logout(request)
    return redirect('homepage')