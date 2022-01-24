from django.db import models
from django.urls import reverse


class Vertolet(models.Model):
    vs_number = models.CharField('Номер ВС', max_length=20)

    def __str__(self):
        return self.vs_number

    def get_absolute_url(self):
        return reverse('machine_detail', kwargs={'vert_id': self.pk})

    class Meta:
        verbose_name = 'Вертолет'
        verbose_name_plural = 'Вертолеты'


class Agregat(models.Model):
    agregat = models.CharField('Прибор', max_length=50)
    date = models.DateField('Дата изготовления')
    update = models.DateField('Дата ремонта')
    vertolet = models.ForeignKey(Vertolet, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.agregat

    class Meta:
        verbose_name = 'Прибор'
        verbose_name_plural = 'Приборы'
