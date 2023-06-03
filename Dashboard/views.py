from django.shortcuts import render
from django.http import HttpResponse
from Dashboard.models import categoriaOcupacional,tipoDiscapacidad,sectorEconomico,rubro,rangoEdades,detalleEstadisticoDiscapacitado

def detail(request):
    return render(request, 'dashboards/dashboard.html')

def categoria(request):
    return render(request, 'dashboards/FormCategoriaOcupacional.html')


def vistaCenso(request):
    return render(request, 'dashboards/censo.html')

def lista_Categoria(request):
    if request.method =='POST':
        nombre = request.POST['categoria']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        categoriaOcupacional.objects.create(
            nombreCategoria=nombre,
            detalle=detalle 
        )
    return render(request,'dashboards/FormCategoriaOcupacional.html')

def lista_Discapacidad(request):

    if request.method =='POST':
        nombre = request.POST['tipoDis']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        tipoDiscapacidad.objects.create(
            nombreDiscapacidad=nombre,
            detalle=detalle 
        )
    return render(request,'dashboards/FormTipoDiscapacidad.html')

def lista_SectorEconomico(request):
    
    if request.method =='POST':
        nombre = request.POST['tipoSecE']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        sectorEconomico.objects.create(
            nombreSector=nombre,
            detalle=detalle 
        )

    return render(request,'dashboards/FormSectorEconomico.html')

def lista_Rubro(request):
     
    if request.method =='POST':
        nombre = request.POST['rubro']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        rubro.objects.create(
             nombreRubro=nombre,
            detalle=detalle 
        )
    return render(request,'dashboards/FormRubro.html')

def lista_RangoEdad(request):
    if request.method =='POST':
        nombre = request.POST['edad']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        rangoEdades.objects.create(
             rangoEdad=nombre,
            detalle=detalle 
        )
    return render(request,'dashboards/FormRangoEdad.html')
