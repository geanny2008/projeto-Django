from django.shortcuts import render , get_object_or_404, redirect
from . import models, forms
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    alunos = models.Aluno.objects.all() # busca todos os objetos (registros) do modelo "Aluno" no banco de dados da sua aplicação Django
    return render(request, 'index.html',{'alunos':alunos})
@login_required
def aluno(request, id): #função de visualização do Django chamada `aluno` que recebe um parâmetro `id`.
    aluno = get_object_or_404(models.Aluno, id=id) #recuperar um único objeto do banco de dados usando a função `get_object_or_404`,parâmetros de pesquisa (neste caso, `id=id`)
    return render(request, 'aluno.html', {'aluno':aluno}) #resposta de view do Django que renderiza um template HTML com um contexto contendo dados a serem exibidos no template.

@login_required
def create(request):
    form = forms.UserForm(request.POST or None, request.FILES or None) # de forms pega models e depois traz para ca

    if form.is_valid():
        form.save() # se for valido tras pro index
        return redirect ('index')
    else:
        return render(request, 'form.html', {'form':form}) # se nao for valido vai retornar para uma mesma pagina do formulario
@login_required
def editar(request,id):
    editar = get_object_or_404(models.Aluno, id=id)
    form = forms.UserForm(request.POST or None, request.FILES or None, instance=editar) 

    if form.is_valid():
        form.save()
        return redirect ('index')
    else:
        return render(request, 'form.html', {'form':form})

@login_required
def deletar(request,id):
    deletar = models.Aluno.objects.get(id=id) # variavel (deletar), vai la em models pega aluno com os objetos deles e pega por id
    deletar.delete()
    return redirect ('index')






