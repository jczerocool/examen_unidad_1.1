from django import forms

class LibroAddForm(forms.Form):
    name = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    ISBN = forms.CharField()
    precio = forms.DecimalField()
    slug = forms.CharField()

def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio <= 100.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio >= 19999.00:
            raise forms.ValidationError("El precio debe ser menor a $19999.00")
        else:
            return precio
