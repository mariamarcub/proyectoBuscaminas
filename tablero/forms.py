from django import forms

class creaTableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas',min_value=1,max_value=20 required=True)
    columnas = forms.IntegerField(label='columnas',min_value=1,max_value=15, required=True)

    #Por defecto el required es TRUE, por lo que no es obligatorio ponerlo en el caso que lo sea