from distutils.command.upload import upload
from django.db import models


class Curso(models.Model):
    titulo = models.CharField("Título", max_length=100)
    vagas = models.IntegerField("Vagas")




class Usuario(models.Model):
    nome_user = models.CharField("Nome", max_length=100)
    cpf = models.CharField("CPF", max_length=11)
    email = models.CharField("Email" , max_length=100)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)

     

class Instituicao(models.Model):
    nome_instituicao = models.CharField("Instituição", max_length=40)
    cnpj = models.CharField("CNPJ", max_length=14)
    telefone = models.CharField("Telefone", max_length=9)
