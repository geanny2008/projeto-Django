from django.shortcuts import render , get_object_or_404
from .models import Aluno

def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html',{'alunos':alunos})

def aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'aluno.html', {'aluno':aluno})
