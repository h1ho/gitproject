from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import Agregat, Vertolet
from .forms import AgregatForm
from django.views.generic import DetailView


class MachineView(LoginRequiredMixin, View):
    def get(self, request):

        agr = Agregat.objects.all()
        vert = Vertolet.objects.all()
        context = {
            'agr': agr,
            'vert': vert,
            'vert_selected': 0,
        }
        return render(request, 'machine/machine.html', context)


class MachineDetailView(DetailView):
    model = Vertolet
    #queryset = Agregat.objects.filter(Vertolet__vs_number='vert_id')
    template_name = 'machine/machine_details.html'
    context_object_name = 'vertolet'
    # РАЗОБРАТСЯ!!!!!!! pk_url_kwarg =


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


#def show_post(request, vert_id):
   # return HttpResponse(f"Отображение статьи с id = {vert_id}")


def show_category(request, vert_id):

    agr = Agregat.objects.filter(vertolet_id=vert_id)
    #agr = Agregat.objects.filter(vertolet__vs_number=)
    vert = Vertolet.objects.all()

    context = {
        'agr': agr,
        'vert': vert,
        'vert_selected': Agregat.vertolet,
    }

    return render(request, 'machine/machine_agr.html', context=context)
