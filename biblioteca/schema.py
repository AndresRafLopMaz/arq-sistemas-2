import strawberry
import strawberry_django
from .models import Autor, Libro


@strawberry_django.type(Autor)
class AutorType:
    id: strawberry.auto
    nombre: strawberry.auto
    correo: strawberry.auto
    edad: strawberry.auto


@strawberry_django.type(Libro)
class LibroType:
    id: strawberry.auto
    titulo: strawberry.auto
    genero: strawberry.auto
    paginas: strawberry.auto
    fecha_publicacion: strawberry.auto
    autor: AutorType


@strawberry.type
class Query:
    autores: list[AutorType] = strawberry_django.field()
    libros: list[LibroType] = strawberry_django.field()


schema = strawberry.Schema(query=Query)