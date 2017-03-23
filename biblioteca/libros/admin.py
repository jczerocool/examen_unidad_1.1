from django.contrib import admin


# Register your models here.

from libros.models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ["ISBN", "autor", "editorial", "precio", "name"]
    list_filter = ["name"]
    search_fields = ["name"]
    list_editable = ["name", "precio"]


    class Meta:
        model = Libro


admin.site.register (Libro, LibroAdmin)
