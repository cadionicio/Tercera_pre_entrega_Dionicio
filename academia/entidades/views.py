from django.shortcuts import render
from .models import *

from .forms import *
# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def curso(request):
    contexto = {"curso": Curso.objects.all()}
    return render(request, "entidades/curso.html",contexto)

def cliente(request):
    contexto = {"cliente": Cliente.objects.all()}
    return render(request, "entidades/cliente.html",contexto)

def compra(request):
    contexto = {"compra": Compra.objects.all()}
    return render(request, "entidades/compra.html",contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")

# Formularios

def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_titulo = miForm.cleaned_data.get("titulo")
            curso_descripcion = miForm.cleaned_data.get("descripcion")
            curso_precio = miForm.cleaned_data.get("precio")

            curso = Curso(titulo=curso_titulo,descripcion=curso_descripcion, precio=curso_precio)
            curso.save()
            contexto = {"curso": Curso.objects.all()}
            return render(request, "entidades/curso.html",contexto)
    else:
        miForm = CursoForm()

    return render(request, "entidades/cursoForm.html", {"form": miForm})

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_usuario = miForm.cleaned_data.get("usuario")
            cliente_password = miForm.cleaned_data.get("password")
            cliente_email = miForm.cleaned_data.get("email")

            cliente = Cliente(nombre=cliente_nombre, usuario=cliente_usuario, password=cliente_password, email=cliente_email)
            cliente.save()
            contexto = {"cliente": Cliente.objects.all()}
            return render(request, "entidades/cliente.html",contexto)
    else:
        miForm = ClienteForm()

    return render(request, "entidades/clienteForm.html", {"form": miForm})

def compraForm(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra_cliente = form.cleaned_data.get("cliente")
            compra_curso = form.cleaned_data.get("curso")

            compra = Compra(cliente=compra_cliente, curso=compra_curso)
            compra.save()
            contexto = {"compra": Compra.objects.all()}
            return render(request, "entidades/compra.html", contexto)
    else:
        form = CompraForm()

    return render(request, "entidades/compraForm.html", {"form": form})

# Buscar

def buscarCurso(request):
    return render(request, "entidades/buscar.html")

def encontrarCurso(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        curso = Curso.objects.filter(titulo__icontains=patron)
        contexto = {'curso': curso}
    else:
        contexto = {'curso': Curso.objects.all()}
    return render(request, "entidades/curso.html", contexto)


