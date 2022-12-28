from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = Create()
        todos = CreateTodo.objects.filter(user = user)
    return render(request, 'home.html',context={'form':form,'todos':todos})

def Register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request,'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/login")
    else:
        return redirect("/login")


def profile(request):
    form = Profile()
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'profile.html', {'form':form})

def create_page(request):
    if request.user.is_authenticated:
        user = request.user
        form = Create(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('/')
    return render(request,'create_todo.html',{'form':form})

def delete_page(request,id):
    form = CreateTodo.objects.get(pk=id).delete()
    return redirect("/")



# Create your views here.
