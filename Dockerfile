# Primera etapa: Construir la imagen base para Django y Poetry
FROM python:3.11 as python-base

# Configuración de variables de entorno
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV DJANGO_SETTINGS_MODULE="config.settings.base"

# Directorio de trabajo
WORKDIR /app

# Copia los archivos de configuración de Poetry
COPY poetry.lock pyproject.toml /app/

# Instala Poetry y las dependencias del proyecto
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia el código fuente de la aplicación
COPY . /app/

# Segunda etapa: Construir la imagen para el servidor de desarrollo de Django
FROM python-base as development-web

# Puerto que usará el servidor de desarrollo de Django
EXPOSE 8000

# Ejecutar migraciones de Django
RUN python manage.py collectstatic --noinput

