from django.shortcuts import render
from .forms import CreaTableroForm

def index(request):
    return render(request, 'tablero/index.html', {})



def crea_tablero(request):
    tablero_form = CreaTableroForm()
    #Si se ha enviado el formulario
    if request.method == 'GET':
        tablero_form = CreaTableroForm(request.GET) #Coge el diccionario q está dentro del request
                                                    #Creo una instancia que le incluye los valores

        #Ejecutamos la validación
        if tablero_form.is_valid(): 
            columnas = tablero_form.cleaned_data['columnas'] #cleaned data es un diccionario q se rellena cuando se hace la validación
            filas = tablero_form.cleaned_data['filas']
            return render(request, 'tablero/muestra_tablero.html', {'filas':filas,'columnas':columnas, 
                                                                            'rango_filas':range(filas), 
                                                                            'rango_columnas':range(columnas) })

    #Si se pide la página por primera vez
    
    return render(request, 'tablero/crea_tablero.html', {'form':tablero_form}) #Este form del context se llama igual que el {{form.as_div}} del crea_tablero