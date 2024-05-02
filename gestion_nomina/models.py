from django.db import models

class Cargo(models.Model):
    id_Cargo = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre
    
class Departamento(models.Model):
    id_Dpto = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre
    
class Tipo_Contrato(models.Model):
    id_TipoContrato = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre
    
class Cuenta_Banco(models.Model):
    id_CuentaBanco = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre

class Personal(models.Model):
    id_Cedula = models.CharField(max_length=20, primary_key=True)
    Nombre_Apellidos = models.CharField(max_length=100)
    Cargo_Empl = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Dpto_Area = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Salario = models.DecimalField(max_digits=12, decimal_places=2)
    Sub_Tpte = models.DecimalField(max_digits=12, decimal_places=2)
    Gastos_Rep = models.DecimalField(max_digits=12, decimal_places=2)
    Sobresueldo = models.DecimalField(max_digits=12, decimal_places=2)
    Viáticos = models.DecimalField(max_digits=12, decimal_places=2)
    Comisiones = models.DecimalField(max_digits=12, decimal_places=2)
    Primas_Pago_Extras = models.DecimalField(max_digits=12, decimal_places=2)
    Tipo_Contr = models.ForeignKey(Tipo_Contrato, on_delete=models.CASCADE)
    Cta_Banco = models.ForeignKey(Cuenta_Banco, on_delete=models.CASCADE)
    Eps_Salud = models.CharField(max_length=100)
    Pensión = models.CharField(max_length=100)
    Fdo_Sol = models.CharField(max_length=100)
    Fecha_Ingreso = models.DateField()
    Fecha_Retiro = models.DateField(null=True)

    def __str__(self):
        return self.Nombre_Apellidos
    
class Devengado(models.Model):
    Concepto = models.CharField(max_length=100, primary_key=True)
    id_Cedula = models.ForeignKey(Personal, on_delete=models.CASCADE)
    Salario = models.DecimalField(max_digits=12, decimal_places=2)
    Sub_Tpte = models.DecimalField(max_digits=12, decimal_places=2)
    Gastos_Rep = models.DecimalField(max_digits=12, decimal_places=2)
    Sobresueldo = models.DecimalField(max_digits=12, decimal_places=2)
    Viáticos = models.DecimalField(max_digits=12, decimal_places=2)
    Comisiones = models.DecimalField(max_digits=12, decimal_places=2)
    Primas_Pago_Extras = models.DecimalField(max_digits=12, decimal_places=2)
    
class Descuento(models.Model):
    Concepto = models.CharField(max_length=100, primary_key=True)
    id_Cedula = models.ForeignKey(Personal, on_delete=models.CASCADE)
    Eps_Salud = models.CharField(max_length=100)
    Pensión = models.CharField(max_length=100)
    Fdo_Sol = models.CharField(max_length=100)
    Bancos = models.CharField(max_length=100)
    Fondo_Empleados = models.CharField(max_length=100)