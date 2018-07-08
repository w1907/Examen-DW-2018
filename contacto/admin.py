from django.contrib import admin
from .models import ContactoUsuario

@admin.register(ContactoUsuario)
class ContactoUsuarioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'email', 'telefono')