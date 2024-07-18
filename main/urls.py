from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('compra', views.compra, name='compra'),
    path('sign_up', views.sign_up, name='signup'),
    path('cartelera', views.cartelera, name='cartelera')
    
    
]