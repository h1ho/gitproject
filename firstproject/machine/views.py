from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Agregat, Vertolet
from .forms import AgregatForm
from django.views.generic import DetailView
from django.db.models import Q


class MachineView(LoginRequiredMixin, View):
    def get(self, request):
        agr = Agregat.objects.all()
        vert = Vertolet.objects.all()
        context = {
            'agr': agr,
            'vert': vert,
            'vsnumber': Agregat.vertolet,
            'vert_selected': 0,
        }
        return render(request, 'machine/machine.html', context)


#  Вывод данных из бд через выборки
class GetRabotyaga(LoginRequiredMixin, View):
    def get(self, request, vert_id):
        vertolet = Vertolet.objects.get(pk=vert_id)
        agregats = Agregat.objects.filter(vertolet_id=vert_id).filter(
            Q(ktodelal_id=request.user.id) | Q(ktodelal_id__isnull=True))
        context = {
            'agregats': agregats,
            'vertolet': vertolet
        }
        return render(request, 'machine/machine_agr.html', context=context)


#  Присвоение имя пользователя к таблице с приборами
class GetAgregatToWork(LoginRequiredMixin, View):
    def post(self, request, agregat_id: int):
        user = request.user
        agr = Agregat.objects.get(pk=agregat_id)
        agr.ktodelal = user
        agr.save()
        return redirect(reverse('vert', kwargs={'vert_id': agr.vertolet_id}))


def create_agr(request, vert_id):
    error = ''
    if request.method == 'POST':
        form = forms.AgregatForm(request.POST, initial={'vertolet': Vertolet.object.get(pk=vert_id)})
        if form.is_valid():
            form.save(commit=False)
            form.vs_number = vert_id
            form.save()
            return redirect('machine')
        else:
            error = 'Неверные данные'
    else:
        form = forms.AgregatForm(initial={'vertolet': Vertolet.object.get(pk=vert_id)})

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'machine/create_agr.html', data)
