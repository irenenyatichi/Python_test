from django import forms
from LogIn.models import User
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


# Create your views here.
def register_user(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegistrationForm()
        print(form.errors)
    return render(request,"index.html",{"form":form})

def create_project(request):
    if request.method=="POST""GET":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegistrationForm()
        print(form.errors)
    return render(request,"index.html",{"form":form})

def start_simulation(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegistrationForm()
        print(form.errors)
    return render(request,"index.html",{"form":form})
