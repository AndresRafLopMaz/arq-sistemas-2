import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from biblioteca.models import Autor, Libro

autor1, _ = Autor.objects.get_or_create(
    correo="gabriel@example.com",
    defaults={
        "nombre": "Gabriel Garcia",
        "edad": 45
    }
)

autor2, _ = Autor.objects.get_or_create(
    correo="ana@example.com",
    defaults={
        "nombre": "Ana Lopez",
        "edad": 38
    }
)

Libro.objects.get_or_create(
    titulo="Introduccion a GraphQL",
    defaults={
        "genero": "Tecnologia",
        "paginas": 220,
        "fecha_publicacion": date(2024, 5, 10),
        "autor": autor1
    }
)

Libro.objects.get_or_create(
    titulo="Bases de Datos Relacionales",
    defaults={
        "genero": "Educativo",
        "paginas": 310,
        "fecha_publicacion": date(2023, 11, 20),
        "autor": autor2
    }
)

print("Datos iniciales cargados correctamente.")