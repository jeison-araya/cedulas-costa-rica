"""
API padrón electoral Costa Rica.
"""
import csv
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
padron.create_index("cedula", unique = True)


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

@app.post("/padron")
def cargar_padron():
    file_path = "tmp/PADRON_COMPLETO.txt"
    
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        headers = [
                "cedula", "codigo_electoral", "relleno",
                "fecha_caducidad", "junta", "nombre",
                "primer_apellido", "segundo_apellido"
                ]
        for row in csv_reader:
            person = {}
            
            for header, value in zip(headers, row):
                if header != "relleno":
                    person[header] = value.strip()

            database["padron"].insert_one(person)
            line_count += 1
        print(f"Rows readed: {line_count}")
        rows_inserted = database["padron"].count_documents({})
        print(f"Rows inserted: {rows_inserted}")
    