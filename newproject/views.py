from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,'newproject/templates/home.html')


# def home_page(request):
#     context={'username':'john'}
#     return render(request,'newproject/templates/home.html',context)

def about_page(request):
    return HttpResponse("<h1>Hello World about</h1>")

def contact_page(request):
    return HttpResponse("<h1>Hello World contact</h1>")