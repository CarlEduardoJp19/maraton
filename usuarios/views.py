from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.

def Principal(request):
    return render(request, 'l')

def registro(request):
    return render(request, 'registro.html')

def BloggerViews(request):
    return render(request, 'Blogger.html')

def login_view(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        clave = request.POST.get("clave")

        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(clave, usuario.clave):
                request.session["usuario_id"] = usuario.id
                messages.succes(request, f"Bienvenido usuario {usuario.correo}")
                return redirect("Blogger")
            else:
                messages.succes(request, "Contraseña incorrecta")
        except Usuario.DoesNotExist:
            messages.error(request, "El usuario no existe")
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        clave = request.POST.get("clave")
        numero = request.POST.get("numero")
        rol = request.POST.get("rol", "lector")

        if Usuario.objects.filter(correo=correo).exists():
            messages.succes(request, "El correo ya existe")
        else:
            usuario = Usuario(
                nombre = nombre,
                correo = correo,
                clave = make_password(clave),
                numero = numero,
                rol = rol
            )
            usuario.save()
            messages.succes(request, "Usuario registrado correctamente")
            return redirect("login")
    return render(request, "registro.html")