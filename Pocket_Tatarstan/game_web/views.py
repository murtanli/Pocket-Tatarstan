from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def levels(request):
    levels = Level.objects.all()
    return render(request, "index.html", {"levels": levels})



def get_level_image(request, level_id):
    level = get_object_or_404(Level, pk=level_id)
    image_path = level.level_image
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

def level_detail(request, level_id):
    parts_of_object = []
    level = get_object_or_404(Level, id=level_id)
    return render(request, "level_game.html", {"level": level})

def level_part_info(request, level_id):
    level = Level.objects.get(id=level_id)
    objects = []
    for obj in level.level_objects.all():  # <-- используем related_name
        parts = [
            {
                "id": part.id,
                "image": part.image.url,
                "center_x": part.center_x,
                "center_y": part.center_y,
            }
            for part in obj.parts.all()
        ]
        objects.append({
            "id": obj.id,
            "name": obj.name,
            "info": getattr(obj, "info", ""),  # если добавишь поле
            "parts": parts
        })

    return JsonResponse({
        "id": level.id,
        "name": level.name,
        "level_image": level.level_image.url if level.level_image else None,
        "objects": objects
    })

def main_page(request):
    return render(request, "index.html")
