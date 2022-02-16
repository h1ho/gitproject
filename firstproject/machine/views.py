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


class GetVertoletIdAndCreate(View):

    def create_agr(self, request, pk):
        error = ''
        if request.method == 'POST':
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
            'error': error,
            'vertolets': vertolets
        }
        return render(request, 'machine/create_agr.html', data)
