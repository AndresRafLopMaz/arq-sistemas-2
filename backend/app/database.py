import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de base de datos.
# Si no existe la variable de entorno DATABASE_URL, usaremos SQLite local
# para desarrollo inicial y pruebas rápidas.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./checklist.db")

# En SQLite, SQLAlchemy necesita este argumento especial.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Engine: componente principal que gestiona la conexión con la base de datos.
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# SessionLocal: fábrica de sesiones para interactuar con la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: clase base para definir nuestros modelos ORM.
Base = declarative_base()


def get_db():
    """
    Generador de sesiones para FastAPI.
    Abre una sesión, la entrega al endpoint y luego la cierra.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()