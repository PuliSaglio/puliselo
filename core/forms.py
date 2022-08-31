from django.forms import ModelForm
from .models import Curso, Instituicao, Usuario


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'vagas']

    ''''''''

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_user', 'cpf', 'email', 'foto']

    ''''''''

class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome_instituicao', 'cnpj', 'telefone']