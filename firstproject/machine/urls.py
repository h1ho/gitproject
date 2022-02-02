from django.urls import path
from . import views  # Из этой же папки ипортируем файл вью

urlpatterns = [
    path('', views.MachineView.as_view(), name='machine'),
    path('create_agr', views.create_agr, name='create_agr'),
    # path('<int:pk>', views.MachineDetailView.as_view(), name='machine_detail'),
    path('vert/<int:vert_id>/', views.GetRabotyaga.as_view(), name='vert'),
    path('agregat/<int:agregat_id>', views.GetAgregatToWork.as_view(), name='vitaskivaem_id'),
]
