from django.urls import path
from . import views


urlpatterns = [
    path("", views.lista_mascotas, name="lista_mascotas"),
    path("agregar/", views.agregar_mascota, name="agregar_mascota"),
    path("propietarios/", views.lista_propietarios, name="lista_propietarios"),
    path("editar/<int:id>/", views.editar_mascota, name="editar_mascota"),
    path("eliminar/<int:id>/", views.eliminar_mascota, name="eliminar_mascota"),
]