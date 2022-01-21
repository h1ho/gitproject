from django.shortcuts import render, redirect
from .models import Agregat
from .forms import AgregatForm


def machine(request):
    agr = Agregat.objects.all()
    return render(request, 'machine/machine.html', {'agr': agr})


def create_agr(request):
    error = ''
    if request.method == 'POST':  # Проверка введенных данных
        form = AgregatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine')
        else:
            error = 'Неверные данные'

    form = AgregatForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'machine/create_agr.html', data)