from django.shortcuts import render, redirect
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


def crear_proyecto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
        )
        return redirect("ver_proyectos")
    return render(request, "proyectos/crear_proyecto.html")


def editar_proyecto(request, proyecto_id):
    try:
        proyecto = Proyecto.objects.get(id=proyecto_id)
    except Proyecto.DoesNotExist:
        return JsonResponse(
            {"error": "Proyecto no encontrado"},
            status=404,
        )

    if request.method == "POST":
        proyecto.nombre = request.POST.get("nombre")
        proyecto.descripcion = request.POST.get("descripcion")
        proyecto.save()
        return redirect("ver_proyectos")

    return render(request, "proyectos/editar_proyecto.html", {"proyecto": proyecto})


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


def crear_tarea(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        proyecto_id = request.POST.get("proyecto_id")
        Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            proyecto_id=proyecto_id,
        )
        return redirect("ver_tareas")
    proyectos = Proyecto.objects.values()
    return render(request, "tareas/crear_tarea.html", {"proyectos": proyectos})


def editar_tarea(request, tarea_id):
    try:
        tarea = Tarea.objects.get(id=tarea_id)
    except Tarea.DoesNotExist:
        return JsonResponse(
            {"error": "Tarea no encontrada"},
            status=404,
        )

    if request.method == "POST":
        tarea.titulo = request.POST.get("titulo")
        tarea.descripcion = request.POST.get("descripcion")
        tarea.proyecto_id = request.POST.get("proyecto_id")
        tarea.save()
        return redirect("ver_tareas")

    proyectos = Proyecto.objects.values()
    return render(
        request, "tareas/editar_tarea.html", {"tarea": tarea, "proyectos": proyectos}
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
