from django.db import models

class ContactoUsuario(models.Model):
	nombre = models.CharField(max_length=45, null=False, blank=False)
	apellido = models.CharField(max_length=45, null=False, blank=False)
	email = models.EmailField()
	telefono = models.CharField(max_length=12, null=False, blank=False)
	direccion = models.CharField(max_length=45, null=False, blank=False)
	comuna = models.CharField(max_length=45, null=True, blank=False)
	imagen = models.ImageField(upload_to='imagen_perfil')

	def __str__(self):
		return self.nombre

	def get_full_direccion(self):
		return '{},{}' . format(self.direccion, self.comuna)