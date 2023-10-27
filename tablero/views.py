from django.shortcuts import render
from .forms import CreaTableroForm

# Create your views here.
def index(request):
    return render(request, 'tablero/index.html', {})

def crea_tablero(request):
    # Si se ha enviado el formulario
    tablero_form = CreaTableroForm()
    if request.method == 'GET':
        tablero_form = CreaTableroForm(request.GET)
        #Ejecutamos la validacion
        if tablero_form.is_valid():
            #Los datos se cogen del diccionario cleaned_data
            columnas = tablero_form.cleaned_data['columnas']
            filas = tablero_form.cleaned_data['filas']
            return render(request, 'tablero/muestra_tablero.html',
                          {'filas':filas,'columnas':columnas,
                                    'rango_filas':range(filas), 'rango_columnas': range(columnas)})
    #Si se pide la página por primera vez
    return render(request, 'tablero/crea_tablero.html', {'form':tablero_form})