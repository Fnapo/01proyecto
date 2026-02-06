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
    if request.method == "POST":
        filtro = request.POST.get("filtro")
        proyectos = Proyecto.objects.filter(nombre__icontains=filtro).values()
    else:
        proyectos = Proyecto.objects.values()
    return render(
        request,
        "proyectos/ver_proyectos.html",
        {
            "proyectos": proyectos,
            "filtro": filtro if request.method == "POST" else None,
        },
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


def detalles_proyecto(request, proyecto_id):
    try:
        proyecto = Proyecto.objects.get(id=proyecto_id)
        return render(
            request, "proyectos/detalles_proyecto.html", {"proyecto": proyecto}
        )
    except Proyecto.DoesNotExist:
        return JsonResponse(
            {"error": "Proyecto no encontrado"},
            status=404,
        )


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


def eliminar_proyecto(request, proyecto_id):
    try:
        proyecto = Proyecto.objects.get(id=proyecto_id)
        if request.method == "POST":
            proyecto.delete()
            return redirect("ver_proyectos")
        return render(
            request, "proyectos/eliminar_proyecto.html", {"proyecto": proyecto}
        )
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
    if request.method == "POST":
        filtro = request.POST.get("filtro")
        tareas = Tarea.objects.filter(titulo__icontains=filtro).values()
    else:
        tareas = Tarea.objects.values()
    return render(
        request,
        "tareas/ver_tareas.html",
        {"tareas": tareas, "filtro": filtro if request.method == "POST" else None},
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


def detalles_tarea(request, tarea_id):
    try:
        tarea = Tarea.objects.get(id=tarea_id)
        return render(request, "tareas/detalles_tarea.html", {"tarea": tarea})
    except Tarea.DoesNotExist:
        return JsonResponse(
            {"error": "Tarea no encontrada"},
            status=404,
        )


def eliminar_tarea(request, tarea_id):
    try:
        tarea = Tarea.objects.get(id=tarea_id)
        if request.method == "POST":
            tarea.delete()
            return redirect("ver_tareas")
        return render(request, "tareas/eliminar_tarea.html", {"tarea": tarea})
    except Tarea.DoesNotExist:
        return JsonResponse(
            {"error": "Tarea no encontrada"},
            status=404,
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
