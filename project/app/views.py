from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    return redirect("https://www.amazon.com/")#to hit url

def form(request):
    return render(request,'home.html')

def register(request):
    print(request.method) #o/p--->'POST' at terminal
    print(request.POST)  #o/p--->query set in key value pair
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    print(name,email,contact)
    Student.objects.create(Name=name, Email=email, Contact=contact)
    print("Data save successfully....")