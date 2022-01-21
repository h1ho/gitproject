from django.db import models


class Agregat(models.Model):
    agregat = models.CharField('Прибор', max_length=50)
    date = models.DateField('Дата изготовления')
    update = models.DateField('Дата ремонта')

    def __str__(self):
        return self.agregat

    class Meta:
        verbose_name = 'Прибор'
        verbose_name_plural = 'Приборы'