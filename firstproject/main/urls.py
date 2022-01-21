from django.urls import path
from . import views  #Из этой же папки ипортируем файл вью

urlpatterns = [
    path('', views.index, name='home'),  #Обращаемся к файлу вью и выводим метод index
    path('about/', views.about, name='about')
]
