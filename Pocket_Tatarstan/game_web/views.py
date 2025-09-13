from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def levels(request):
    levels = Level.objects.all()
    return render(request, "levels.html", {"levels": levels})



def get_level_image(request, level_id):
	level = get_object_or_404(Level, pk=level_id)
	image_path = level.level_image
	return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

def level_detail(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    return render(request, "level_game.html", {"level": level})