# Assignment 07 - API GraphQL

## Descripción
Proyecto desarrollado con Django, Strawberry GraphQL y PostgreSQL desplegado en Render.

## Endpoint público
https://assignment-07-graphql.onrender.com/graphql/

## Modelos disponibles

### Modelo: Autor

| Campo  | Tipo    | Descripción |
|--------|---------|-------------|
| id     | Integer | Identificador único del autor |
| nombre | String  | Nombre del autor |
| correo | String  | Correo electrónico del autor |
| edad   | Integer | Edad del autor |

### Modelo: Libro

| Campo              | Tipo    | Descripción |
|-------------------|---------|-------------|
| id                | Integer | Identificador único del libro |
| titulo            | String  | Título del libro |
| genero            | String  | Género del libro |
| paginas           | Integer | Número de páginas |
| fechaPublicacion  | Date    | Fecha de publicación |
| autor             | Autor   | Relación con el autor |

## Consultas de ejemplo

### Obtener autores
```graphql
query {
  autores {
    id
    nombre
    correo
    edad
  }
}
```

### Obtener Libros
```graphql
query {
  libros {
    id
    titulo
    genero
    paginas
    fechaPublicacion
  }
}
```

### Obtener Libros Con Autor
```graphql
query {
  libros {
    titulo
    autor {
      nombre
      correo
    }
  }
}
```

# Datos de Prueba Cargados
### Autores
- Gabriel Garcia
- Ana Lopez

### Libros
- Introduccion a GraphQL
- Bases de Datos Relacionales

### Tecnologías utilizadas
- Python
- Django
- Strawberry GraphQL
- PostgreSQL
- Render
