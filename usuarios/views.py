from django.shortcuts import render

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    return render(request, 'usuarios/logout.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
# Create your views here.
