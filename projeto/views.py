from django.shortcuts import render , get_object_or_404, redirect
from . import models, forms

def index(request):
    alunos = models.Aluno.objects.all()
    return render(request, 'index.html',{'alunos':alunos})

def aluno(request, id):
    aluno = get_object_or_404(models.Aluno, id=id)
    return render(request, 'aluno.html', {'aluno':aluno})


def create(request):
    form = forms.UserForm(request.POST or None, request.FILES or None) # de forms pega models e depois traz para ca

    if form.is_valid():
        form.save() # se for valido tras pro index
        return redirect ('index')
    else:
        return render(request, 'form.html', {'form':form}) # se nao for valido vai retornar para uma mesma pagina do formulario

def editar(request,id):
    editar = get_object_or_404(models.Aluno, id=id)
    form = forms.UserForm(request.POST or None, request.FILES or None, instance=editar) 

    if form.is_valid():
        form.save()
        return redirect ('index')
    else:
        return render(request, 'form.html', {'form':form})


def deletar(request,id):
    deletar = models.Aluno.objects.get(id=id) # variavel (deletar), vai la em models pega aluno com os objetos deles e pega por id
    deletar.delete()
    return redirect ('index')