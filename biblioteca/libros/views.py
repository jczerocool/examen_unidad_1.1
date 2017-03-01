from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Libro
from .forms import LibroAddForm

# Create your views here.

def home(request):
    h = "hello biblioteca jajjaj"
    contexto = {"mensaje1": h}
    return render(request, "home.html", contexto)


def lista_libros(request):
    libros = Libro.objects.all()
    h = "libros existentes"
    template = "listadelibros.html"
    contexto = {"mensaje1": h, "libros": libros}
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):
    perros = get_object_or_404(Libro, id=object_id)
    h = "libro nuevo"
    template = "detalle.html"
    contexto = {"mensaje1": h, "libros": perros}
    return render(request, template, contexto)

def agregar_libro(request):
    form = LibroAddForm(request.POST or None)
    if request.POST == "POST":
        print request.POST
    if form.is_valid():
        print "good"
        #print request.POST#
        data = form.cleaned_data
        name = data.get("name")
        autor = data.get("autor")
        editorial = data.get("editorial")
        ISBN = data.get("ISBN")
        precio = data.get("precio")
        slug = data.get("slug")

        print name
        print autor
        print editorial
        print ISBN
        print precio
        print slug

        nuevo_libro = Libro()
        nuevo_libro.name = name
        nuevo_libro.autor = autor
        nuevo_libro.editorial = editorial
        nuevo_libro.ISBN = ISBN
        nuevo_libro.precio = precio
        nuevo_libro.slug = slug
        nuevo_libro.save()

    template = "agregar_libro.html"
    context = {"form": form}
    return render(request, template, context)


def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        libros = get_object_or_404(Libro, slug=slug)
    except Libro.MultipleObjectsReturned:
        libros = Producto.objects.filter(slug=slug).order_by("-name").first()

    print Libro
    m = "libro nuevo"
    template = "detalle_slug.html"
    contexto= {"mensaje": m, "libros": libros}
    return render(request, template, contexto)




"""
def detalle_s(request, slug=None):
    try:
        librosprueba = get_object_or_404(Libro, slug=slug)
    except Libro.MultipleObjectsReturned:
        librosprueba = Libro.objects.filter(slug=slug).order_by("-nombre").first()
    m = "libro nuevo"
    template = "detalle.html"
    contexto = {"mensaje": m, "Libro": librosprueba}
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    try:
        librosprueba = get_object_or_404(Libro, slug=slug)
    except Libro.MultipleObjectsReturned:
        librosprueba = Libro.objects.filter(slug=slug).order_by("-nombre").first()
    m = "libro nuevo"
    template = "detalle.html"
    contexto = {"mensaje": m, "Libro": librosprueba}
    return render(request, template, contexto)

"""
"""
def detalle(request, object_id=None):
    libro = get_object_or_404
    h = "nuevo detalle"
    template = "detalle.html"
    contexto = {"mensaje1": h, "libro": libro}
    return render(request, template, contexto)
"""

"""def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(Producto, id=object_id)
    m = "productos nuevo"
    template = "detalle_libro.html"
    contexto= {"mensaje":m,
           "libro": libro }
    return render(request, template, contexto)"""





"""def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    producto = get_object_or_404(Producto, id=object_id)
    m = "productos nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
           "producto": producto }
    return render(request, template, contexto)

    # if object_id is not None:
    #     try:
    #         producto = Producto.objects.get(id=object_id)
    #         m = "productos nuevo"
    #         template = "detalle.html"
    #         contexto= {"mensaje":m,
    #                "producto": producto }
    #         return render(request, template, contexto)
    #     except Producto.DoesNotExist:
    #         producto = None
    #         m = "productos nuevo"
    #         template = "detalle.html"
    #         contexto= {"mensaje":m,
    #                "producto": producto }
    #         return render(request, template, contexto)"""
