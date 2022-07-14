# api-padron-electoral-costa-rica
API para consultar el padrón electoral generado por el Tribunal Supremo de Elecciones de Costa Rica


# Configuración local

1. Crear un entorno virtual en python
    - `python -m venv venv`
2. Activar entorno virtual
    - Windows: `.\venv\Scripts\activate`
    - Linux o Mac: `source venv/bin/activate`

3. Instalar dependecias
    - `pip install -r requirements.txt`

4. Ejecutar API
    - `uvicorn api.main:app --reload`

