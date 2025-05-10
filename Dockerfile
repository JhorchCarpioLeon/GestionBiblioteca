# Usamos Python oficial como base
FROM python:3.13.0 

# Establecer el directorio de trabajo en el contenedor
WORKDIR /Froned

# Copiar requirements.txt primero (mejora la caché si no cambia)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto del contenedor
EXPOSE 8000

# Comando para ejecutar la app con gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

