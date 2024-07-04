from django.db import models

# Modelo de negocio de la Aplicacion
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre}"

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo}"

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f"{self.cliente} - {self.curso}"