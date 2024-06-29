from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect("https://www.amazon.com/")#to hit url

def form(request):
    return render(request,'home.html')

def register(request):
    print(request.method)
    print(request.POST)
