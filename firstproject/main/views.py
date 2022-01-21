from django.shortcuts import render
from django.http import HttpResponse

#метод выводит данные html
def index(request):
    return render(request, 'main/index.html') #метод render выводит html шаблон


def about(request):
    return render(request, 'main/about.html')
