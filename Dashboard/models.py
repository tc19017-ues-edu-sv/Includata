from django.db import models

# Create your models here.

class detalleEstadisticoDiscapacitado(models.Model):
    cantidadHombre=models.IntegerField()
    cantidadMujeres=models.IntegerField()

    def __str__(self):
        return f"Hombres: {self.cantidadHombre} Mujeres: {self.cantidadMujeres}"

class tipoDiscapacidad(models.Model):
    id= models.AutoField(primary_key=True)
    nombreDiscapacidad=models.CharField(max_length=30,verbose_name="Nombre Discapacidad")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
	    return self.nombreDiscapacidad
    
    
class sectorEconomico(models.Model):
    
    nombreSector=models.CharField(max_length=30,verbose_name="Nombre Sector")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreSector
    
class rubro(models.Model):
    nombreRubro=models.CharField(max_length=30,verbose_name="Nombre Rubro")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombreRubro

class categoriaOcupacional(models.Model):
   
    nombreCategoria=models.CharField(max_length=30,verbose_name="Nombre Categoria")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombreCategoria

class rangoEdades(models.Model):
    rangoEdad=models.CharField(max_length=5,verbose_name="Rango Edad")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.rangoEdad
    