# Generated by Django 5.0.2 on 2024-05-05 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_Cargo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta_Banco',
            fields=[
                ('id_CuentaBanco', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_Dpto', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Contrato',
            fields=[
                ('id_TipoContrato', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_Cedula', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nombre_Apellidos', models.CharField(max_length=100)),
                ('Salario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Sub_Tpte', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Gastos_Rep', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Sobresueldo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Viáticos', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Comisiones', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Primas_Pago_Extras', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Eps_Salud', models.CharField(max_length=100)),
                ('Pensión', models.CharField(max_length=100)),
                ('Fdo_Sol', models.CharField(max_length=100)),
                ('Fecha_Ingreso', models.DateField()),
                ('Fecha_Retiro', models.DateField(null=True)),
                ('Cargo_Empl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionN.cargo')),
                ('Cta_Banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionN.cuenta_banco')),
                ('Dpto_Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionN.departamento')),
                ('Tipo_Contr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionN.tipo_contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Devengado',
            fields=[
                ('Concepto', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Salario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Sub_Tpte', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Gastos_Rep', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Sobresueldo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Viáticos', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Comisiones', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Primas_Pago_Extras', models.DecimalField(decimal_places=2, max_digits=12)),
                ('id_Cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionN.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('Concepto', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Eps_Salud', models.CharField(max_length=100)),
                ('Pensión', models.CharField(max_length=100)),
                ('Fdo_Sol', models.CharField(max_length=100)),
                ('Bancos', models.CharField(max_length=100)),
                ('Fondo_Empleados', models.CharField(max_length=100)),
                ('id_Cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionN.personal')),
            ],
        ),
    ]