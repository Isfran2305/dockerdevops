#Paso 1   
FROM python:3.12-alpine

#Paso 2

WORKDIR /app

#Paso 3

COPY requirements.txt /app

#Paso 4

RUN pip install --no-cache-dir -r requirements.txt

#Paso 5

COPY  app.py /app

#Paso 6

EXPOSE 5000

#Paso 7

CMD ["python", "app.py"]
