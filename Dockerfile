FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask psycopg2-binary
COPY templates/ /app/templates/  # Esto asegura que la carpeta templates se copie
CMD ["python", "app.py"]
