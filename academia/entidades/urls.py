from django.urls import path, include
from entidades.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),

    path('acerca/', acerca, name="acerca"),

    #____ Curso
    path('cursoForm/', cursoForm, name="cursoForm"),
    path('curso', curso, name="curso"),
    path('cursoUpdate/<id_curso>/', cursoUpdate, name="cursoUpdate"),
    path('cursoDelete/<id_curso>/', cursoDelete, name="cursoDelete"),

    #____ Cliente
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('cliente', cliente, name="cliente"),
    path('clienteUpdate/<id_cliente>/', clienteUpdate, name="clienteUpdate"),
    path('clienteDelete/<id_cliente>/', clienteDelete, name="clienteDelete"),

    #____ Compra
    path('compraForm/', compraForm, name="compraForm"),
    path('compra', compra, name="compra"),
    path('compraUpdate/<id_compra>/', compraUpdate, name="compraUpdate"),
    path('compraDelete/<id_compra>/', compraDelete, name="compraDelete"),

    #____ Buscar
    path('buscarCurso/', buscarCurso, name="buscarCurso"),
    path('encontrarCurso/', encontrarCurso, name="encontrarCurso"),

    #___ Login/ Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #___ Edicion de Perfil / Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(),name="cambiarClave"),
    path('agregar_avatar', agregarAvatar, name="agregar_avatar"),
]
