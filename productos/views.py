from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Paleta
from django.urls import reverse_lazy


class CrearPaleta(CreateView):
    model = Paleta
    template_name = "productos/crear_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['modelo', 'marca', 'fecha']

class ListadoPaletas(ListView):
    model = Paleta
    template_name = "productos/listado_paletas.html"
    context_object_name = 'paletas'
    
class VerPaleta(DetailView):
    model = Paleta
    template_name = "productos/ver_paleta.html"

class EditarPaleta(UpdateView):
    model = Paleta
    template_name = "productos/editar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['modelo', 'marca', 'fecha']
    
class EliminarPaleta(DeleteView):
    model = Paleta
    template_name = "productos/eliminar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')

