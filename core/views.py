from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import LoginForm, UserRegisterForm
from .models import Record


def homepage_view(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'homepage.html', {'records': records})
    else:
        return redirect('login')



def record_view(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, pk=pk)
        return render(request, 'record.html', {'record': record})
    else:
        redirect('login')


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


def register_view(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
    