from django.shortcuts import render, redirect

from Person.forms import CustomerForm, PersonComplainForm, RegistrationForm, RegisterForm

from django.contrib import messages


def login(request):
    form = RegistrationForm()
    return render(request, 'login.html', {"form":form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        form = RegisterForm()
        messages.success(request, 'Student registered successful')
        return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form":form})

def index(request):
    form = PersonComplainForm()
    return render(request, 'index.html', {"form":form})

def aboutus(request):
    form = CustomerForm()
    return render(request, 'aboutus.html',{"form":form})
