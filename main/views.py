from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    context={"clase": "inicio"}
    return render(request, 'index.html')

def about(request):
    context={"clase": "about"}
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
    if request.method != "POST":
        context={"clase": "registro"}
        return render(request, 'sign_up.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'sign_up.html', context)
    

def cartelera(request):
    context={"clase": "cartelera"}
    return render(request, 'cartelera.html')

def compra(request):
    context={"clase": "compra"}
    return render(request, 'compra.html')

def login(request):
    context={"clase": "login"}
    return render(request, 'registration/login.html')

def agregarAlCarrito(request, product_name):
    if 'cart' not in request.session:
        request.session['cart'] = []
    
    cart = request.session['cart']
    cart.append(product_name)
    request.session['cart'] = cart
    messages.success(request, f'{product_name} ha sido agregado con éxito')
    return redirect('carrito')

def carrito(request):
    cart = request.session.get('cart', [])
    context = {
        'cart': cart
    }
    return render(request, 'carrito.html', context)