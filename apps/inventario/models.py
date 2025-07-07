from django.db import models
#models
class Categoria(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    def __str__(self):
        return f"{self.nombre}"
class Producto(models.Model):
    nombre= models.CharField(max_length=100)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=300)
    precio=models.IntegerField()
    stock_disponible=models.IntegerField()

    def __str__(self):
        return f"{self.nombre},{self.categoria}"