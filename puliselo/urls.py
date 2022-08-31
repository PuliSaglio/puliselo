"""puliselo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from core import views
from core.views import cadastrar_instituicao, cadastrar_usuario, editar_instituicao, editar_usuario, listar_cursos, cadastrar_curso, editar_curso, listar_instituicoes, listar_usuarios, remover_curso, remover_instituicao, remover_usuario

urlpatterns = [
    path('' , views.index),
    #path('instituicoes/' , views.instituicao, name='instituicao'),
    #path('cursos/' , views.cursos, name='cursos'),
   #path('usuarios/' , views.usuario, name='usuario'),
   #path('admin/', admin.site.urls),
    
    path('cursos/', listar_cursos, name='listar_cursos'),
    path('cadastrar_curso/', cadastrar_curso, name='cadastrar_curso'), 
    path('editar_curso/<int:id>/', editar_curso, name='editar_curso'),
    path('remover_curso/<int:id>/', remover_curso, name='remover_curso'),
    path('usuarios/', listar_usuarios, name='listar_usuario'), 
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'), 
    path('usuario_editar/<int:id>/', editar_usuario, name='editar_usuario'),
    path('usuario_remover/<int:id>/', remover_usuario, name='remover_usuario'),
    path('instituicoes/', listar_instituicoes, name='listar_instituicoes'), 
    path('cadastrar_instituicao/', cadastrar_instituicao, name='cadastrar_instituicoes'),
    path('instituicao_editar/<int:id>/', editar_instituicao, name='editar_instituicao'),
    path('instituicao_remover/<int:id>/', remover_instituicao, name='remover_instituicao'), 
    ]

    
    
