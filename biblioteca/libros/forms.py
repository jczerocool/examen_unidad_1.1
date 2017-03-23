from django import forms

from .models import Libro

OPCIONES_TIPO = (
    ('foto', "Foto"),
    ('video juego', "Video Juego"),
    ('libro', "Libro"),
)

class LibroAddForm(forms.Form):
    name = forms.CharField(label="Nombre del libro",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Ponga el nombre'}))
    autor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    editorial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ISBN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField()


def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio <= 100.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio >= 19999.00:
            raise forms.ValidationError("El precio debe ser menor a $19999.00")
        else:
            return precio

class LibroModelForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=OPCIONES_TIPO)
    class Meta:
        model = Libro
        fields =[
            "name",
            "autor",
            "editorial",
            "ISBN",
            "precio"
        ]
        labels = {
            "name": "Cual es nombre del libro",
            "autor":"Cual es el nombre del ",
            "precio":"Cual es precio del libro"
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Ponga el nombre'}),
            "descripcion": forms.Textarea(attrs={'class': 'form-control'}),
            "precio": forms.NumberInput(attrs={'class': 'form-control'}),

        }

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio <= 100.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio >= 19999.00:
            raise forms.ValidationError("El precio debe ser menos que $19999.00")
        else:
            return precio
