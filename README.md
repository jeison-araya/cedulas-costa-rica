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

# Actualizar padrón utilizando mongoimport

## Requerimientos:
- Instalar [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/installation/installation/)
    - Recuerda agregar al PATH (Windows) y/o brindar los permisos necesarios (Linux o Mac).
- Descargar el [padrón electoral completo](https://www.tse.go.cr/descarga_padron.htm)
- Ejecutar el siguiente comando:
    `mongoimport -h <hostname><:port> --u <username> --p <password> -d <database>  -c padron --authenticationDatabase=admin --type csv -f cedula,codigo_electoral,relleno,fecha_caducidad,junta,nombre,primer_apellido,segundo_apellido --file PADRON_COMPLETO.txt 
    `