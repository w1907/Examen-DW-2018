from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ContactoUsuario

class ContactoList(ListView):
	model = ContactoUsuario
	template_name = 'vista_contacto/contacto.html'

class ContactoDetail(DetailView):
	model = ContactoUsuario
	template_name = 'vista_contacto_detalle/contacto_detalle.html'