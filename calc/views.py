from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def home(request):
 #   return HttpResponse("<h1>Hello Mrigendra !<h1>")

def home(request):
    return render(request, 'calc/dashboard.html')

def products(request):
    return render(request, 'calc/products.html')


def customer(request):
    return render(request, 'calc/customer.html')