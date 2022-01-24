from django.urls import path
from . import views  # Из этой же папки ипортируем файл вью

urlpatterns = [
    path('', views.machine, name='machine'),
    path('create_agr', views.create_agr, name='create_agr'),
    path('<int:pk>', views.MachineDetailView.as_view(), name='machine_detail')
]
