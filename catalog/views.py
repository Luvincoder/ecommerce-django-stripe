from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')

def details(request):
    return render(request, 'details.html')

def faq(request):
    return render(request, 'faq.html')

def registration(request):
    return render(request, 'registration.html')

def shop(request):
    return render(request, 'shop.html')