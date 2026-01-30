from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Tarea

# Create your views here.


def hola(request, nombre="invitado"):
    return HttpResponse(f"Hola Mundo a {nombre} desde miapp01")


def index(request):
    return render(
        request,
        "index.html",
    )


def proyectos(request):
    lista_proyectos = list(Proyecto.objects.values())
    return JsonResponse(
        lista_proyectos,
        safe=False,
    )


def ver_proyectos(request):
    proyectos = Proyecto.objects.values()
    return render(
        request,
        "proyectos/ver_proyectos.html",
        {"proyectos": proyectos},
    )


def buscar_proyecto(request, proyecto_id):
    try:
        proyecto = Proyecto.objects.values().get(id=proyecto_id)
        """
        proyecto_data = {
            "id": proyecto["id"],
            "nombre": proyecto["nombre"],
            "descripcion": proyecto["descripcion"],
        }
        """
        return JsonResponse(proyecto)
    except Proyecto.DoesNotExist:
        return JsonResponse(
            {"error": "Proyecto no encontrado"},
            status=404,
        )


def tareas(request):
    lista_tareas = list(Tarea.objects.values())
    return JsonResponse(
        lista_tareas,
        safe=False,
    )


def ver_tareas(request):
    tareas = Tarea.objects.values()
    return render(
        request,
        "tareas/ver_tareas.html",
        {"tareas": tareas},
    )


def buscar_tarea(request, tarea_id):
    try:
        tarea = Tarea.objects.values().get(id=tarea_id)
        return JsonResponse(tarea)
    except Tarea.DoesNotExist:
        return JsonResponse(
            {"error": "Tarea no encontrada"},
            status=404,
        )
