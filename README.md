# Usando base datos con driver Python-MongoDB

# Requisitos
1. Tener una version de python 3.10 en adelante instalada
2. Instalar: "sudo apt install python3-pip"
3. Instalar pymongo: "sudo pip install pymongo"
4. Instalar start mongod: "sudo systemctl start mongod"

# Instalacion correcta de entorno virtual

1. Instalar modulo entornos virtuales: apt install python3−venv
2. Crear entorno virtual: python3 −m venv venv−python3
3. Activar entorno virtual: source venv−python3/activate


# Pasos para su ejecucion

1. Descargar codigo
2. Instalar dependencias pip
3. Ejecutar comando: sudo systemctl start mongod
4. En carpeta ejecutar comando: source active
5. Ejecutar comando: python main.py  



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
