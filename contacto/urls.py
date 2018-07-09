from django.urls import path
from .views import ContactoList, ContactoDetail

urlpatterns = [
	path('', ContactoList.as_view(), name="contacto.home"),
	path('detalle/<int:pk>', ContactoDetail.as_view(), name="contacto.detail")
]