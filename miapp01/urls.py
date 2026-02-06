from django.urls import path
from . import views

ulrspatterns = [
    path("hola/<str:nombre>/", views.hola),
    path("", views.hola),
    path("index", views.index, name="index"),
    path("proyectos/", views.proyectos, name="proyectos"),  # el name para hrefs
    path("proyectos/<int:proyecto_id>/", views.buscar_proyecto),
    path("ver_proyectos/", views.ver_proyectos, name="ver_proyectos"),
    path("crear_proyecto/", views.crear_proyecto, name="crear_proyecto"),
    path(
        "detalles_proyecto/<int:proyecto_id>/",
        views.detalles_proyecto,
        name="detalles_proyecto",
    ),
    path(
        "editar_proyecto/<int:proyecto_id>/",
        views.editar_proyecto,
        name="editar_proyecto",
    ),
    path(
        "eliminar_proyecto/<int:proyecto_id>/",
        views.eliminar_proyecto,
        name="eliminar_proyecto",
    ),
    path("tareas/", views.tareas, name="tareas"),
    path("tareas/<int:tarea_id>/", views.buscar_tarea),
    path("ver_tareas/", views.ver_tareas, name="ver_tareas"),
    path("crear_tarea/", views.crear_tarea, name="crear_tarea"),
    path("detalles_tarea/<int:tarea_id>/", views.detalles_tarea, name="detalles_tarea"),
    path(
        "editar_tarea/<int:tarea_id>/",
        views.editar_tarea,
        name="editar_tarea",
    ),
    path(
        "eliminar_tarea/<int:tarea_id>/",
        views.eliminar_tarea,
        name="eliminar_tarea",
    ),
]
