from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def acerca(request):
    return render(request, "entidades/acerca.html")


# ___ Curso
@login_required
def curso(request):
    contexto = {"curso": Curso.objects.all()}
    return render(request, "entidades/curso.html",contexto)

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

def cursoUpdate(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso.titulo = miForm.cleaned_data.get("titulo")
            curso.descripcion = miForm.cleaned_data.get("descripcion")
            curso.precio = miForm.cleaned_data.get("precio")
            curso.save()
            contexto = {"curso": Curso.objects.all() }
            return render(request, "entidades/curso.html", contexto)       
    else:
        miForm = CursoForm(initial={"titulo": curso.titulo, "descripcion": curso.descripcion, "precio": curso.precio}) 
    return render(request, "entidades/cursoForm.html", {"form": miForm})

def cursoDelete(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    contexto = {"curso": Curso.objects.all() }
    return render(request, "entidades/curso.html", contexto)

# ___ Cliente
@login_required
def cliente(request):
    contexto = {"cliente": Cliente.objects.all()}
    return render(request, "entidades/cliente.html",contexto)

@login_required
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

@login_required
def clienteUpdate(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.usuario = miForm.cleaned_data.get("usuario")
            cliente.password = miForm.cleaned_data.get("password")
            cliente.email = miForm.cleaned_data.get("email")
            cliente.save()
            contexto = {"cliente": Cliente.objects.all()}
            return render(request, "entidades/cliente.html", contexto)
    else:
        miForm = ClienteForm(initial={"nombre":cliente.nombre,
                                      "usuario":cliente.usuario,
                                      "password":cliente.password,
                                      "email":cliente.email})
    return render(request, "entidades/clienteForm.html", {"form": miForm})

@login_required
def clienteDelete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    contexto = {"cliente": Cliente.objects.all() }
    return render(request, "entidades/cliente.html", contexto)


# __Compra
@login_required
def compra(request):

    contexto = {"compra": Compra.objects.all()}
    return render(request, "entidades/compra.html",contexto)

@login_required
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

@login_required
def compraUpdate(request, id_compra):
    compra = Compra.objects.get(id=id_compra)
    if request.method == "POST":
        miForm = CompraForm(request.POST)
        if miForm.is_valid():
            compra.cliente = miForm.cleaned_data.get("cliente")
            compra.curso = miForm.cleaned_data.get("curso")
            compra.save()
            contexto = {"compra": Compra.objects.all()}
            return render(request, "entidades/compra.html", contexto)
    else:
        miForm = CompraForm(initial={"cliente":compra.cliente,
                                      "curso":compra.curso})
    return render(request, "entidades/compraForm.html", {"form": miForm})

@login_required
def compraDelete(request, id_compra):
    compra = Compra.objects.get(id=id_compra)
    compra.delete()
    contexto = {"compra": Compra.objects.all() }
    return render(request, "entidades/compra.html", contexto)

# Buscar

@login_required
def buscarCurso(request):
    return render(request, "entidades/buscar.html")

@login_required
def encontrarCurso(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        curso = Curso.objects.filter(titulo__icontains=patron)
        contexto = {'curso': curso}
    else:
        contexto = {'curso': Curso.objects.all()}
    return render(request, "entidades/curso.html", contexto)


#____ Login / Logout  / Registrarion

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user )

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    
    return render(request, "entidades/registro.html", {"form": miForm})

#__ Edicion de Perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            
            # Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            # Crear un nuevo avatar
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            # Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})
