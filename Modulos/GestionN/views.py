from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def inicioDeSesion(request):
    if request.method == 'POST':
        username = request.POST.get('SuperAdmin')
        password = request.POST.get('%SuperAdmin2024%')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicioDeSesion')
        else:
            return render(request, 'inicioDeSesion.html', {'error': True})
    return render(request ,'inicioDeSesion.html')
        
def cerrarSesion(request):
    logout(request)
    return redirect('inicioDeSesion')
