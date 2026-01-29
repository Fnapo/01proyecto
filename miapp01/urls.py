from django.urls import path
from . import views

ulrspatterns = [
    path("hola/<str:nombre>/", views.hola),
    path("", views.hola),
    path("index", views.index, name="index"),
    path("proyectos/", views.proyectos, name="proyectos"),  # el name para hrefs
    path("proyectos/<int:proyecto_id>/", views.buscar_proyecto),
    path("ver_proyectos/", views.ver_proyectos, name="ver_proyectos"),
    path("tareas/", views.tareas, name="tareas"),
    path("tareas/<int:tarea_id>/", views.buscar_tarea),
]
