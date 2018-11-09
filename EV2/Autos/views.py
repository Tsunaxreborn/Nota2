from django.shortcuts import render
from django.utils import timezone
from .models import Automovil


def post_list(request):
    post = Automovil.objetcs.filter(Fecha_publicacion__lte=timezone.now()).order_by('Fecha_publicacion')
    return render(request, 'templates/Autos/post_list.html', {'posts':post})