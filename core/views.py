from django.shortcuts import render, redirect
from .models import Curso, Instituicao, Usuario
from .forms import CursoForm, InstituicaoForm, UsuarioForm

#Links para as páginas

def index(request):
    return render(request, "index.html")
    
def cursos(request):
    return render(request, "cursos.html")

def instituicao(request):
    return render(request, "instituicoes.html")

def usuario(request):
    return render(request, "usuarios.html")

#Funçoes de cursos

def listar_cursos(request):
    
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }

    
    return render(request, 'cursos.html', contexto)

def cadastrar_curso(request):
    form = CursoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_cursos')

    contexto = {
    'form_curso' : form
    }

    return render(request, 'cadastrar_curso.html', contexto)

def editar_curso(request, id):
        curso = Curso.objects.get(pk=id)

        form = CursoForm(request.POST or None, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

        contexto = {
            'form_curso': form
        }

        return render(request, 'cadastrar_curso.html', contexto)

def remover_curso(request, id):
        curso = Curso.objects.get(pk=id)
        curso.delete()
        return redirect('listar_cursos')

 
#Funcoes Usuarios


def listar_usuarios(request):
    
    usuarios = Usuario.objects.all()
    contexto = {
        'usuarios': usuarios
    }

    return render(request, 'usuarios.html', contexto)


def cadastrar_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')

    contexto = {
    'form_usuario' : form
    }

    return render(request, 'cadastrar_usuario.html', contexto)

def editar_usuario(request, id):
        usuario = Usuario.objects.get(pk=id)

        form = UsuarioForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

        contexto = {
            'form_usuario': form
        }

        return render(request, 'cadastrar_usuario.html', contexto)

def remover_usuario(request, id):
        usuario = Usuario.objects.get(pk=id)
        usuario.delete()
        return redirect('listar_usuario')


#Funcoes das Insituiçoes


def listar_instituicoes(request):
    
    instituicoes = Instituicao.objects.all()
    contexto = {
        'instituicoes': instituicoes
    }

    
    return render(request, 'instituicoes.html', contexto)


def cadastrar_instituicao(request):
    form = InstituicaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_instituicoes')

    contexto = {
    'form_instituicoes' : form
    }
    return render(request, 'cadastrar_instituicao.html', contexto)

def editar_instituicao(request, id):
        instituicao = Instituicao.objects.get(pk=id)

        form = InstituicaoForm(request.POST or None, instance=instituicao)
        if form.is_valid():
            form.save()
            return redirect('listar_instituicoes')

        contexto = {
            'form_instituicoes': form
        }

        return render(request, 'cadastrar_instituicao.html', contexto)

def remover_instituicao(request, id):
        instituicao = Instituicao.objects.get(pk=id)
        instituicao.delete()
        return redirect('listar_instituicoes')