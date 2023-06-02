from django.contrib import admin
from django.urls import path, include
from Dashboard.views import *

urlpatterns = [
    path('includata/dashboard/', detail),
    path('admin/', admin.site.urls),
    
]
