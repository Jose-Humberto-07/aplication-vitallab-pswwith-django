from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.



def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais, por favor, tente novamente.')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter 7 ou mais dígitos, por favor, tente novamente.')
            return redirect('/usuarios/cadastro')
        
        try:

            user = User.objects.create_user(
                    first_name = primeiro_nome,
                    last_name = ultimo_nome,
                    username = username,
                    email = email,
                    password = senha
            )

            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso.')
        except:
            messages.add_message(request, constants.ERROR, 'Erro: erro interno do sistema.')
            return redirect('/usuarios/cadastro')

        return redirect('/usuarios/cadastro')
    


def logar(request):
    
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login(request, user)
            return redirect('/') # falta criar essa página
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/usuarios/login')

        return HttpResponse(f'{username} e {senha}')