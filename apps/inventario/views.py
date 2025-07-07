from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/list.html'
    context_object_name = 'Categoria'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'categoria/create.html'
    success_url = reverse_lazy('categoria:categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = 'categoria/update.html'
    success_url = reverse_lazy('categoria:categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/delete.html'
    success_url = reverse_lazy('categoria:categoria_list')

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/list.html'
    context_object_name = 'producto'

class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'producto/create.html'
    success_url = reverse_lazy('producto:producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'producto/update.html'
    success_url = reverse_lazy('producto:producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/delete.html'
    success_url = reverse_lazy('producto:producto_list')
