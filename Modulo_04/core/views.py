from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm # 1. Importe o form
from django.contrib.auth import login # 2. Importe a função 'login'
from django.contrib.auth.decorators import login_required # 1. Importe o decorador
from .models import Tarefa
from .forms import TarefaForm




@login_required  # 2. Adicione o decorador aqui
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
    if form.is_valid():
        tarefa = form.save(commit=False)
        tarefa.user = request.user
        tarefa.save()
        return redirect('home')
    else:
        form = TarefaForm()

    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')

    context = {
        'nome_usuario': request.user.username,  # Use o nome do usuário logado!
        'tecnologias': ['Autenticação', 'ForeignKey', 'Login'],
        'tarefas': todas_as_tarefas,
        'form': form,
    }
    return render(request, 'home.html', context)    

@login_required
def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save()
        return redirect('home')
    
@login_required
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'register.html', context)