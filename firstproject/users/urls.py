from django.urls import path
from . import views  # Из этой же папки ипортируем файл вью

urlpatterns = [
    path('', views.users_enter, name='users_enter'),
    path('users_reg', views.users_reg, name='users_reg')
]
