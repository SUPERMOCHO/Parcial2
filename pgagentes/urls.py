"""pgagentes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from core.views import registro, Modificar_registro, Eliminar_registro, registronom_agente, Modificar_Agente, Eliminar_registroAgente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/', registro),
    path('Modificar_registro/<int:id>/', Modificar_registro),
    path('Eliminar_registro/<int:id>/', Eliminar_registro),
    path('Registronom_agente/', registronom_agente),
    path('Modificar_Agente/<int:id>/', Modificar_Agente),
    path('Eliminar_registroAgente/<int:id>/', Eliminar_registroAgente),
    path('accounts/', include ('django.contrib.auth.urls')),   

    ]
