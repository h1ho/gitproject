from django.urls import path
from . import views  # Из этой же папки ипортируем файл вью
from .views import RegisterView, LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='account_enter'),
    path('registrations/', RegisterView.as_view(), name='account_reg')
]
