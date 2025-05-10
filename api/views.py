from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor  # Asegúrate de que el modelo se llama así

def vista_autores(request):
    autores = Autor.objects.all()
    autor = None

    if 'editar' in request.GET:
        autor = get_object_or_404(Autor, id=request.GET['editar'])

    if 'eliminar' in request.GET:
        Autor.objects.filter(id=request.GET['eliminar']).delete()
        return redirect('vista_autores')

    if request.method == 'POST':
        data = request.POST
        if data.get('id'):
            autor = get_object_or_404(Autor, id=data['id'])
            autor.nombre = data['nombre']
            autor.apellido = data['apellido']
            autor.nacionalidad = data['nacionalidad']
            autor.fecha_nacimiento = data['fecha_nacimiento']
            autor.biografia = data['biografia']
            autor.save()
        else:
            Autor.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                nacionalidad=data['nacionalidad'],
                fecha_nacimiento=data['fecha_nacimiento'],
                biografia=data['biografia']
            )
        return redirect('vista_autores')

    return render(request, 'autores.html', {'autores': autores, 'autor': autor})
## Para libros
from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro

# Vista para mostrar todos los libros, y manejar la edición y eliminación
def vista_libros(request):
    libros = Libro.objects.all()

    # Editar un libro
    if 'editar' in request.GET:
        libro_id = request.GET['editar']
        libro = get_object_or_404(Libro, id=libro_id)
        return render(request, 'libros.html', {'libros': libros, 'libro': libro})

    # Eliminar un libro
    if 'eliminar' in request.GET:
        libro_id = request.GET['eliminar']
        libro = get_object_or_404(Libro, id=libro_id)
        libro.delete()
        return redirect('vista_libros')  # Redirige a la lista de libros después de eliminar

    # Lógica para agregar o editar libro cuando se envía el formulario
    if request.method == 'POST':
        libro_id = request.POST.get('id')  # Se obtiene el ID del libro
        
        if libro_id:
            # Editar libro
            libro = get_object_or_404(Libro, id=libro_id)
            libro.titulo = request.POST['titulo']
            libro.autor = request.POST['autor']
            libro.fecha_publicacion = request.POST['fecha_publicacion']
            libro.genero = request.POST['genero']
            libro.descripcion = request.POST['descripcion']
            libro.save()
        else:
            # Agregar un nuevo libro
            Libro.objects.create(
                titulo=request.POST['titulo'],
                autor=request.POST['autor'],
                fecha_publicacion=request.POST['fecha_publicacion'],
                genero=request.POST['genero'],
                descripcion=request.POST['descripcion']
            )
        
        return redirect('vista_libros')  # Redirige a la lista de libros después de agregar o editar

    return render(request, 'libros.html', {'libros': libros})


