from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('success')  
    else:
        form = Contact()

    return render(request, 'contact.html', {'form': form})
    
    

def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def cartelera(request):
    return render(request, 'cartelera.html')

def compra(request):
    return render(request, 'compra.html')


def success_view(request):
    return render(request, 'success.html')