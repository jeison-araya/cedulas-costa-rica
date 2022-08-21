# api-padron-electoral-costa-rica
API para consultar el padrón electoral generado por el Tribunal Supremo de Elecciones de Costa Rica


# Requisitos

1. Instancia de `MongoDB`.
2. Instalar `Python 3.10 o superior` o `Docker`


# Configuración local

## Utilizando python
1. Crear un entorno virtual en python
    - `python -m venv venv`
2. Activar entorno virtual
    - Windows: `.\venv\Scripts\activate`
    - Linux o Mac: `source venv/bin/activate`

3. Instalar dependecias
    - `pip install -r requirements.txt`

4. Crear archivo con variables
    - Crear archivo de configuración: `cp .example.env .env`
    - Reemplaza los valores del archivo `.env`

5. Ejecutar API
    - `uvicorn api.main:app --reload`


## Utilizando docker-compose
1. Crear archivo con variables
    - Crear archivo de configuración: `cp .example.env .env`
    - Reemplaza los valores del archivo `.env`

2. Ejecutar `docker-compose up -d`

# Actualizar padrón utilizando mongoimport

## Requerimientos:
- Instalar [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/installation/installation/)
    - Recuerda agregar al PATH (Windows) y/o brindar los permisos necesarios (Linux o Mac).
- Descargar el [padrón electoral completo](https://www.tse.go.cr/descarga_padron.htm)
- Ejecutar el siguiente comando:
    `mongoimport -h <hostname><:port> -u <username> -p <password> -d <database>  -c padron --authenticationDatabase=admin --type csv -f cedula,codigo_electoral,relleno,fecha_caducidad,junta,nombre,primer_apellido,segundo_apellido --file PADRON_COMPLETO.txt 
    `


    # Deployments

    ## Heroku

    Este proyecto tiene la configuración necesaria para realizar deployments en Heroku.

    - El archivo `Procfile` contiene la instrucción para ejecutar el API.

    - El `runtime.txt` contiene la versión de python a utilizar.  

## Pruebas

### Estética del código con Pylint

- Verifica que se cumplan las convenciones de PEP 8.
- Ejecutar el siguiente comando: `pylint api`