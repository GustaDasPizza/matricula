from django.shortcuts import render, get_object_or_404,redirect
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def aluno_listar(request):
    alunos = Aluno.objects.all()
    context ={
        'alunos':alunos
    }
    return render(request, "base.html",context)

def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Aluno salvo com sucesso")
        else:
            print(form.errors)
    else:
        form = AlunoForm()

    return render(request, "forms.html", {'form': form})

def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,request.FILES,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'forms.html',{'form':form})

def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar')

def aluno_detalhes(request, id):
    alunos = get_object_or_404(Aluno, id=id)
    return render(request, "detalhes.html", {"alunos": alunos})