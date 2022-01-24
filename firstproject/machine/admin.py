from django.contrib import admin
from .models import Agregat, Vertolet

admin.site.register(Agregat)


class AgregatInline(admin.TabularInline):
    model = Agregat


@admin.register(Vertolet)
class VertoletAdmin(admin.ModelAdmin):
    inlines = [
        AgregatInline
    ]
