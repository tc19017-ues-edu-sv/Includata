from django.db import models

# Create your models here.
class tipoDiscapacidad(models.Model):
    
    nombreDiscapacidad=models.CharField(max_length=30,verbose_name="Nombre Discapacidad")
    
    def __str__(self):
	    return self.nombreDiscapacidad
    
    
class sectorEconomico(models.Model):
    
    nombreSector=models.CharField(max_length=30,verbose_name="Nombre Sector")
    
    def __str__(self):
        return self.nombreSector
    
class rubro(models.Model):
    
    nombreRubro=models.CharField(max_length=30,verbose_name="Nombre Rubro")
    
    def __str__(self):
        return self.nombreRubro

class categoriaOcupacional(models.Model):
   
    nombreCategoria=models.CharField(max_length=30,verbose_name="Nombre Categoria")
    
    def __str__(self):
        return self.nombreCategoria