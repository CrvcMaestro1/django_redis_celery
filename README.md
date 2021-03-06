# Django x Redis x Celery

## Configurar .ENV

Agregar SECRET_KEY a .env (usar de referencia a .env.example)

## Instalar dependencias

Primero creamos el entorno virtual:

```bash
python3 -m venv venv
```

Lo activamos:

```bash
env/Scripts/activate
```

Lanzamos el comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Docker

Primero necesitaremos descargar las imágenes de postgres y redis:

```bash
docker pull postgres
docker pull redis
```

Ahora solo necesitamos arrancar los contenedores para realizar las pruebas:

```bash
docker run --rm -p 5433:5432 --name testpostgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin123 -e POSTGRES_DB=test postgres
docker run --rm -p 6379:6379 --name testredis redis
```

## Migrar tablas y generar datos

Para realizar las pruebas, necesitaremos migrar las tablas a postgres:

```bash
python manage.py migrate
```

Después creamos el super usuario para posteriormente crear los posts:

```bash
python manage.py createsuperuser
```

Por último lanzamos el archivo script.py para cargar datos en la tabla post.

```bash
python script.py
```