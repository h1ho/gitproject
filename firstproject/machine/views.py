from django.shortcuts import render, redirect
from .models import Agregat, Vertolet
from .forms import AgregatForm
from django.views.generic import DetailView


def machine(request):
    agr = Agregat.objects.all()
    vert = Vertolet.objects.all()
    return render(request, 'machine/machine.html', {'agr': agr, 'vert': vert})


class MachineDetailView(DetailView):
    model = Vertolet
    # queryset = Agregat.objects.filter(vert_id)
    template_name = 'machine/machine_details.html'
    context_object_name = 'vertolet'
    # pk_url_kwarg =

    def get_queryset(self):
        # РАЗОБРАТСЯ!!!!!!! return Agregat.objects.filter(vertolet__.kwards['vertolet_'])


def create_agr(request):
    error = ''
    if request.method == 'POST':  # Проверка введенных данных
        form = AgregatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine')
        else:
            error = 'Неверные данные'
    else:
        form = AgregatForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'machine/create_agr.html', data)
