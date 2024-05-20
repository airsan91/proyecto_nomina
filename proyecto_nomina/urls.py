"""
URL configuration for proyecto_nomina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Modulos.GestionN import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicioDeSesion/', views.inicioDeSesion, name='inicioDeSesion'),
    path('cerrarSesion/', LogoutView.as_view(), name='cerrarSesion'),
    path('', views.inicioDeSesion, name='home'),
    path('personal/', views.personal_view, name='personal'),
    path('editar_personal/<int:id_Cedula>/', views.edit_personal, name='editar_personal'),
    path('detalle_personal/<int:id_Cedula>/', views.detail_personal, name='detalle_personal'),
    path('delete_personal/<int:id_Cedula>/', views.delete_personal, name='delete_personal'),
    path('create_superuser/', views.create_superuser),
    path('crearEmpleado/', views.crearEmpleado, name='crearEmpleado'),
]
