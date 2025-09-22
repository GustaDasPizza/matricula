from django.db import models

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    nasc = models.DateField()
    sexo = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=250)
    uf = models.CharField(max_length=2)
    matricula = models.CharField(max_length=150)
    curso = models.CharField(max_length=250)
    serie = models.IntegerField()
    turno = models.CharField(max_length=150)
    observacoes = models.TextField()
