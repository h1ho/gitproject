from django.urls import path
from . import views  # Из этой же папки ипортируем файл вью

urlpatterns = [
    path('login', views.account_enter, name='account_enter'),
    path('registrations/', views.account_reg, name='account_reg'),
    path('logout/', views.logout_user, name='logout')

]
