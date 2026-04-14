from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=80)
    paginas = models.PositiveIntegerField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='libros'
    )

    def __str__(self):
        return self.titulo