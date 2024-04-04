# Usando base datos con driver Python-MongoDB

# Requisitos
1. Tener una version de python 3.10 en adelante instalada
2. Instalar pymongo: "sudo pip install pymongo"
3. Instalar start mongod: "sudo systemctl start mongod"


# Pasos para su ejecucion

1. Descargar codigo
2. Posicionarse en carpeta /bin
3. Instalar dependencias pip
4. Ejecutar comando: sudo systemctl start mongod
5. En carpeta ejecutar comando: source active
6. Ejecutar comando: python main.py  

# Usos
- Este programa tiene como objeto probar bases de datos no relacionales a través de librerías como "mongod" a través de una collection llamada "tareas"


# Base de datos
En la base de datos se recopilan datos teoricos de diversas actividades como tareas que se deben de cubrir en cierto establecimiento:
- Tarea: Descripcion de la tarea a realizar
- Encargado: Persona que realizara la tarea
- Fecha: Tiempo en que se deberá cumplir dicha tarea
- Estado: En que proceso actulamente se encuentra la tarea
- https://ibb.co/FJCf06G

# Archivos de uso
- main.py: contiene el codigo base de la logica de programa
- database.json: collection de base de datos que puede ser consumida y/o importada
