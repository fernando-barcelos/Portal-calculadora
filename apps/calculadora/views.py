from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login.models import Usuario
from .models import Operacao

def index(request):
    #Vericia se o usuário está autenticado
    if not request.session.get('usuario_id'):
        messages.error(request, 'Você precisa estar logado para acessar esta página.')
        return redirect('login')  # Redireciona para a página de login se não estiver autenticado
    
    pegaTresUltimasOperacoes = Operacao.objects.filter(idusuario=request.session.get('usuario_id')).order_by('-dtinclusao')[:3] # Obtém as três últimas operações do usuário

    return render(request, 'calculadora/index.html', { 'operacoes': pegaTresUltimasOperacoes }) # ja traz as 3 ultimas operações do usuário autenticado

def calcular(request):
    if request.method == 'POST':
        usuario = request.session.get('usuario_id')# Obtém o usuário autenticado
        usuarioDB = Usuario.objects.get(idusuario=usuario)
        
        try:
            expressao = request.POST.get('expressao_digitada', '') #parametro
            calculo = request.POST.get('resultado_final', '') #resultado
            if not expressao:
                raise ValueError("A expressão não pode estar vazia.")
            
            novaOperacao = Operacao(idusuario=usuarioDB, #cria uma nova operação
                                    parametros=expressao,
                                    resultado=calculo)
            
            novaOperacao.save()  # Salva a operação no banco de dados

            pegaTresUltimasOperacoes = Operacao.objects.filter(idusuario=request.session.get('usuario_id')).order_by('-dtinclusao')[:3] # Obtém as três últimas operações do usuário

            return render(request, 'calculadora/index.html', { 'operacoes': pegaTresUltimasOperacoes, 'calculo': calculo })  # Renderiza a página com o resultado do cálculo e as últimas operações
        except ValueError as e:
            messages.error(request, str(e))
    
    return redirect('index')  # Redireciona para a página inicial se houver erro ou método não for POST