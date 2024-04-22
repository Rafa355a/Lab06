from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Fecha de Registro')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Fecha de Registro')
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
