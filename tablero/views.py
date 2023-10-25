from django.shortcuts import render

def index(request):
    return render(request, 'tablero/index.html', {})



def crea_tablero(request):
    return render(request, 'tablero/crea_tablero.html', {})