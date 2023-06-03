from django.contrib import admin
from django.urls import path, include
from Dashboard.views import *

urlpatterns = [
    path('includata/dashboard/', detail),
    path('admin/', admin.site.urls),
    path('includata/dashboards/censo/', vistaCenso),
    path('includata/dashboards/FormCategoriaOcupacional/', lista_Categoria, name='lista_Categoria'),
    path('includata/dashboards/FormTipoDiscapacidad/', lista_Discapacidad, name='lista_Discapacidad'),
    path('includata/dashboards/FormSectorEconomico/', lista_SectorEconomico, name='lista_SectorEconomico'),
    path('includata/dashboards/FormRubro/', lista_Rubro, name='lista_Rubro'),
    path('includata/dashboards/FormRangoEdad/', lista_RangoEdad, name='lista_RangoEdad'),
    
]
