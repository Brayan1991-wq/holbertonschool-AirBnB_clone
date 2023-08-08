#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Clase base que define atributos y métodos comunes para otras clases.

    Atributos de instancia pública:
    id (str):
    Identificación única generada al crear una instancia.
    created_at (datetime):
    Fecha y hora de creación de la instancia.
    updated_at (datetime):
    Fecha y hora de la última actualización de la instancia.

    Métodos de instancia pública:
    __str__():
    Devuelve una representación en cadena del objeto.
    save():
    Actualiza el atributo updated_at con la fecha y hora actual.
    to_dict():
    Devuelve un diccionario con los atributos
    de la instancia en formato serializable.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase ModeloBase.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
