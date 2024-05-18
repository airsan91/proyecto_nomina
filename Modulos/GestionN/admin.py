from django.contrib import admin
from .models import Cargo, Personal, Cuenta_Banco, Departamento, Descuento, Devengado, Tipo_Contrato

admin.site.register(Cargo)
admin.site.register(Personal)
admin.site.register(Cuenta_Banco)
admin.site.register(Departamento)
admin.site.register(Descuento)
admin.site.register(Devengado)
admin.site.register(Tipo_Contrato)