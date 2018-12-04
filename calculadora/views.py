from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import formularioCal


def index(request):
    if request.method == 'POST':
        form = formularioCal(request.POST)
        if form.is_valid():
            numuno = form.cleaned_data['numeroUno']
            numdos = form.cleaned_data['numeroDos']
            suma = calcularLocal(numuno, numdos)
            ctx = {'form': form, 'rta': suma, 'n1': numuno, 'n2': numdos}
        # return HttpResponseRedirect('calcular/'+str(numuno)+'/'+str(numdos))
        return render(request, 'calculadora/formulario.html', ctx)
    form = formularioCal()
    ctx = {'form': form}
    return render(request, 'calculadora/formulario.html', ctx)


def calcularLocal(a, b):
    return a + b


def calcular(request, num_uno, num_dos):
    suma = num_uno + num_dos
    ctx = {
        'suma': suma,
        'num1': num_uno,
        'num2': num_dos
    }
    return render(request, "calculadora/inicio.html", ctx)


def gracias(request):
    return HttpResponse("Gracias")
