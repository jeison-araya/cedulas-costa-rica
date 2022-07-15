"""
API padrón electoral Costa Rica.
"""
from fastapi import FastAPI, HTTPException, status
from api.database import database
from api.schemas import Persona

app = FastAPI()

exceptions = {
    "PersonaNoEncontrada": HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail="E001: Persona no encontrada"),
    "FormatoCedulaNoValida": HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                         detail="E002: Formato de cédula no válido"),
}


padron = database["padron"]


@app.get("/padron/cedula/{cedula:int}", response_model=Persona)
def obtener_por_cedula(cedula: int):
    """
    GET - Obtener persona por número de cédula.

    Formato de la cédula: numero de cédula sin guiones, sin puntos y longitud igual a 9.
    """
    if 1000000000 < cedula > 9999999999:
        raise exceptions["FormatoCedulaNoValida"]

    persona = padron.find_one({"cedula": cedula})

    if not persona:
        raise exceptions["PersonaNoEncontrada"]

    return persona
