from django.urls import path
from .views import CategoriaCreateView,CategoriaListView,CategoriaDeleteView,CategoriaUpdateView
from .views import ProductoCreateView,ProductoDeleteView,ProductoListView,ProductoUpdateView

app_name="inventario"

urlpatterns=[
    path("categoria/",CategoriaListView.as_view(),name="categoria_list"),
    path("nuevo/",CategoriaCreateView.as_view(),name="categoria_create"),
    path("<int:pk>/editar/",CategoriaUpdateView.as_view(),name="categoria_update"),
    path("<int:pk>/eliminar/",CategoriaDeleteView.as_view(),name="categoria_delete"),

    path("categoria/",ProductoListView.as_view(),name="producto_list"),
    path("nuevo/",ProductoCreateView.as_view(),name="producto_create"),
    path("<int:pk>/editar/",ProductoUpdateView.as_view(),name="producto_update"),
    path("<int:pk>/eliminar/",ProductoDeleteView.as_view(),name="producto_delete"),
]