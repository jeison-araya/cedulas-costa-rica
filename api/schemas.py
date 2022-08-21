# pylint: disable=no-name-in-module
# pylint: disable=too-few-public-methods
"""
Schemas classes
"""
from pydantic import BaseModel


class Persona(BaseModel):
    """
    Persona

    Representa una persona que pertence al padrón electoral.

    Atributos:

    - cedula: Número de cédula del ciudadano sin guiones,
              sin puntos y longitud igual a 9.
    - nombre: Nombre completo del ciudadano
    - primer_apellido: Primer apellido
    - segundo_apellido Segundo apellido
    """
    cedula: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
