from django.contrib import admin

# Register your models here.
from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "precio")
    list_filter = ("titulo",)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "usuario", "password", "email")
    list_filter = ("nombre",)

class CompraAdmin(admin.ModelAdmin):
    list_display = ("cliente", "curso", "fecha_compra")
    list_filter = ("cliente", "curso", "fecha_compra",)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Compra, CompraAdmin)
