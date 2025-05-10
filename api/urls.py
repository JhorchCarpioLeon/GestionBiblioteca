from django.urls import path
from .views import vista_autores, vista_libros

urlpatterns = [
    path('', vista_autores, name='vista_autores'),  # Redirige a la vista_autores en la raíz de la app
    path('libros/', vista_libros, name='vista_libros'),  # Ruta para la vista_libros
]
