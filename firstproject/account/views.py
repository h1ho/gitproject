from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import AccEnter, AccReg


def account_enter(request):
    error = ''

    if request.method == 'POST':
        form = AccEnter(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Неверный логин или пароль'
    else:
        form = AccEnter()

    return render(request, 'account/account_enter.html', {'form': form, 'error': error})


def account_reg(request):
    if request.method == 'POST':
        form = AccReg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AccReg()
    return render(request, 'account/account_reg.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('account_enter')
