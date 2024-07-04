from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('curso', curso, name="curso"),
    path('cliente', cliente, name="cliente"),
    path('compra', compra, name="compra"),

    path('acerca/', acerca, name="acerca"),

    #Formulario
    path('cursoForm/', cursoForm, name="cursoForm"),
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('compraForm/', compraForm, name="compraForm"),

    path('buscarCurso/', buscarCurso, name="buscarCurso"),
    path('encontrarCurso/', encontrarCurso, name="encontrarCurso"),
]
