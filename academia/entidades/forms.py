from django import forms

from .models import *

class CursoForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(widget=forms.Textarea, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    usuario = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=False)

class CompraForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)