from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import PersonalForm
from .models import Personal
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse

def create_superuser(request):
    User.objects.create_superuser('SuperAdmin', None ,'%SuperAdmin2024%')
    return HttpResponse("Superuser created.")


def crearEmpleado(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal')
    else:
        form = PersonalForm()
    return render(request, 'CrearEmpleado.html', {'form': form})


def inicioDeSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('personal')
        else:
            return render(request, 'inicioDeSesion.html', {'error': True})
    return render(request ,'inicioDeSesion.html')
        
def cerrarSesion(request):
    logout(request)
    return render('inicioDeSesion.html')

def personal_view(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal')
    else:
        form = PersonalForm()
    personals = Personal.objects.all()
    return render(request, 'personal.html', {'form': form, 'personals': personals})

def edit_personal(request, id_Cedula):
    personal = get_object_or_404(Personal, id_Cedula=id_Cedula)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('personal')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'editar_personal.html', {'form': form, 'empleado': personal})


def detail_personal(request, id_Cedula):
    personal = get_object_or_404(Personal, id_Cedula=id_Cedula)
    return render(request, 'detalle_personal.html', {'personal': personal})



def delete_personal(request, id_Cedula):
    personal = get_object_or_404(Personal, id_Cedula=id_Cedula)
    personal.delete()
    return redirect('home')