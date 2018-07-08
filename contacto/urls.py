from django.urls import path
from .views import ContactoList

urlpatterns = [
	path('', ContactoList.as_view(), name="contacto.home"),
]