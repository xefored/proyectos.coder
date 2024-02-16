from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.PositiveBigIntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
    
class Destinos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveBigIntegerField("$")
    
    def __str__(self):
        return self.nombre
    

class Hoteles(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    precio = models.PositiveBigIntegerField("$")
    descripcion=models.TextField(null=True, blank=True, verbose_name="descripciòn" )
    
    def __str__(self):
        return self.nombre
    
     
    



class Viaje(models.Model):
    nombre = models.CharField(max_length=100)
    destino = models.ForeignKey(Destinos, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(Hoteles, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.nombre}-{self.destino}-{self.hotel}-{"GASTO TOTAL: $"}{self.hotel.precio + self.destino.precio }"
    
        
    

class clientes_viajes(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.cliente}-{self.viaje}"
    
    
    
    
    