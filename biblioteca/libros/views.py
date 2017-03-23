from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

#unidad tres
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Libro
from .forms import LibroAddForm, LibroModelForm

# Create your views here.
def home(request):

    m = "Hola biblio hahha"
    contexto = {"mensaje": m}
    return render(request, 'home.html', contexto)


class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroModelForm
    success_url = "/libros/crear/"

    def get_context_data(self, *args, **kwargs):
        context = super(LibroCreateView, self).get_context_data(*args, **kwargs)
        return context

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroModelForm
    success_url = "/libros/update/"

    def get_context_data(self, *args, **kwargs):
        context = super(LibroUpdateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Editar"
        return context

class LibroDetailView(DetailView):
    model = Libro

class LibroListView(ListView):
    model = Libro

    def get_queryset(self, *args, **kwargs):
        qs = super(LibroListView, self).get_queryset(**kwargs)
        return qs


def lista_libros(request):
    #Logico de negocio alias hechizo
    libros = Libro.objects.all()
    print request
    m = "libros nuevos"
    template = "listadelibros.html"
    contexto = {"mensaje": m, "libros": libros}
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        libros = get_object_or_404(Libro, slug=slug)
    except Libro.MultipleObjectsReturned:
        libros = Libro.objects.filter(slug=slug).order_by("-name").first()

    print Libro
    m = "libros nuevo"
    template = "detalle.html"
    contexto = {"mensaje": m, "libros": libros}
    return render(request, template, contexto)


def detalle_s(request, slug=None):
    #Logico de negocio alias hechizo
    try:
        Libro = get_object_or_404(Libro, slug=slug)
    except Libro.MultipleObjectsReturned:
        libros = Libro.objects.filter(slug=slug).order_by("-name").first()
    m = "libros nuevos"
    template = "detalle.html"
    contexto = {"mensaje": m, "libros": libros}
    return render(request, template, contexto)

def agregar_libro(request):
    #FORM
    form = LibroAddForm(request.POST or None)
    if request.method == "POST":
        print request.POST
    if form.is_valid():
        # print request.POST
        data = form.cleaned_data
        name = data.get("name")
        autor = data.get("autor")
        editorial = data.get("editorial")
        ISBN = data.get("ISBN")
        precio = data.get("precio")
        # nuevo_producto = Producto.object.create(nombre = nombre,
        #                                         descripcion = descripcion,
        #                                         precio = precio)
        nuevo_libro = Libro()
        nuevo_libro.name = name
        nuevo_libro.autor = autor
        nuevo_libro.editorial = editorial
        nuevo_libro.ISBN = ISBN
        nuevo_libro.precio = precio

        nuevo_libro.save()

    template = "agregar_libro.html"
    context = {"form": form}


    return render(request, template, context)



def update(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404 (Libro, id = object_id)
    form = LibroModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "update.html"
    contexto= {
           "libro": libros,
           "form": form,
           "titulo":" Actualizar Libro"
           }
    return render(request, template, contexto)


def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(Libro, id=object_id)
    m = "libros nuevos"
    template = "detalle.html"
    contexto = {"mensaje": m, "libros": libros}
    return render(request, template, contexto)
