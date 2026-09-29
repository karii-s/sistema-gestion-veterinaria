from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mascota, Propietario
from .forms import MascotaForm, PropietarioForm


@login_required
def lista_mascotas(request):
    mascotas = Mascota.objects.all()

    return render(request, "veterinaria/lista_mascotas.html", {
        "mascotas": mascotas
    })


@login_required
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


@login_required
def lista_propietarios(request):
    propietarios = Propietario.objects.all()

    return render(request, "veterinaria/lista_propietarios.html", {
        "propietarios": propietarios
    })


@login_required
def agregar_propietario(request):
    if request.method == "POST":
        form = PropietarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_propietarios")
    else:
        form = PropietarioForm()

    return render(request, "veterinaria/agregar_propietario.html", {
        "form": form
    })


@login_required
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


@login_required
def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":
        mascota.delete()
        return redirect("lista_mascotas")

    return render(request, "veterinaria/eliminar_mascota.html", {
        "mascota": mascota
    })