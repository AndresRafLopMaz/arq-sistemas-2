from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """
    Schema base compartido por creación y actualización.
    """
    title: str = Field(..., min_length=1, max_length=150)
    description: Optional[str] = None


class TaskCreate(TaskBase):
    """
    Schema para crear una tarea.
    Hereda title y description.
    """
    pass


class TaskUpdate(BaseModel):
    """
    Schema para actualizar una tarea.
    Todos los campos son opcionales para permitir PATCH parcial.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=150)
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskResponse(BaseModel):
    """
    Schema de salida para responder desde la API.
    """
    id: int
    title: str
    description: Optional[str]
    is_completed: bool
    created_at: datetime

    class Config:
        from_attributes = True