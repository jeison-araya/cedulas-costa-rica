"""
API padrón electoral Costa Rica.
"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from api.database import database

app = FastAPI()

exceptions = {
    "PersonaNoEncontrada": HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail="E001: Persona no encontrada"),
    "FormatoCedulaNoValida": HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                         detail="E002: Formato de cédula no válido"),
}


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


padron = database["padron"]

@app.get("/padron/cedula/{cedula:int}", response_model=Persona)
def obtener_por_cedula(cedula: int):
    """
    GET - Obtener persona por número de cédula.

    Formato de la cédula: numero de cédula sin guiones, sin puntos y longitud igual a 9.
    """
    if cedula < 1000000000 or cedula > 9999999999:
        raise exceptions["FormatoCedulaNoValida"]

    persona = padron.find_one({"cedula": cedula})

    if not persona:
        raise exceptions["PersonaNoEncontrada"]

    return persona
