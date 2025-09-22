from django import forms
from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'nasc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000000000'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000000'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2, 'placeholder': 'UF'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de matrícula'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Curso'}),
            'serie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Série'}),
            'turno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Turno'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações'}),
        }
