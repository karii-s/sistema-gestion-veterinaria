from django.shortcuts import render, redirect
from .models import Mascota, Propietario
from .forms import MascotaForm


def lista_mascotas(request):
    mascotas = Mascota.objects.all()

    return render(request, "veterinaria/lista_mascotas.html", {
        "mascotas": mascotas
    })


def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_mascotas")
    else:
        form = MascotaForm()

    return render(request, "veterinaria/agregar_mascota.html", {
        "form": form
    })


def lista_propietarios(request):
    propietarios = Propietario.objects.all()

    return render(request, "veterinaria/lista_propietarios.html", {
        "propietarios": propietarios
    })


def editar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":
        form = MascotaForm(request.POST, instance=mascota)

        if form.is_valid():
            form.save()
            return redirect("lista_mascotas")
    else:
        form = MascotaForm(instance=mascota)

    return render(request, "veterinaria/editar_mascota.html", {
        "form": form,
        "mascota": mascota
    })


def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":
        mascota.delete()
        return redirect("lista_mascotas")

    return render(request, "veterinaria/eliminar_mascota.html", {
        "mascota": mascota
    })