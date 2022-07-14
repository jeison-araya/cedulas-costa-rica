from fastapi import FastAPI, HTTPException, status
from api.database import database

app = FastAPI()

exceptions = {
    "PersonaNoEncontrada": HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail="E001: Persona no encontrada")
}


@app.get("/padron/cedula/{cedula:str}")
def obtener_por_cedula(cedula: str):
    
    persona = database["padron"].find_one({"cedula": cedula})
    
    if not persona:
        raise exceptions["PersonaNoEncontrada"]
    
    return persona
