from django.shortcuts import render, redirect
from .forms import PessoaForm 

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/formulario.html', {'form': form})

def sucesso(request):
    return render(request, 'cadastro/sucesso.html')
