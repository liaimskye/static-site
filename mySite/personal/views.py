from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'personal_home.html')

def product(request):
    return render(request,'product_page.html')

def info(request):
    return render(request,'personal_info.html')