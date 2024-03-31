from pymongo import MongoClient
import json
from bson import json_util  # Importa json_util para manejar ObjectId

# Conectarse a la base de datos local de MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Seleccionar una base de datos (si no existe, se creará automáticamente)
db = client['mydatabase']

# Crear una colección llamada 'mycollection'
collection = db['tareas']

# Insertar un documento en la colección
def Insertar ():
    post = {'tarea': 'Lavar trastes', 'encargado': 'Juan Carlos Gonzalez', 'fecha': '2020-05-01', 'estado': 'pendiente'}
    collection.insert_one(post)
    print('----Documento insertado exitosamente----')


# Modificar un documento en la colección
def Modificar ():
    query = {'tarea': 'Lavar trastes'}
    new_values = {'$set': {'estado': 'realizado'}}
    collection.update_one(query, new_values)
    print('----Documento modificado exitosamente----')


# Eliminar un documento de la colección
def Eliminar ():
    query = {'tarea': 'Lavar trastes'}
    collection.delete_one(query)
    print('----Documento eliminado exitosamente----')

# Mostrar todos los documentos en la colección
def Ver ():
    for post in collection.find():
        print(post)
        
        
# Exportar la base de datos actual en formato JSON
def Exportar():
    # Obtener todos los documentos de la colección
    documents = collection.find()
    # Crear una lista para almacenar los documentos
    data = []
    for document in documents:
        # Convertir ObjectId a una cadena serializable
        document['_id'] = str(document['_id'])
        data.append(document)
    # Escribir los documentos en un archivo JSON
    with open('database.json', 'w') as file:
        # Usar json_util para serializar los documentos a JSON
        json.dump(data, file, default=json_util.default)
    print('----Base de datos exportada exitosamente----')

#Llamadas de las acciones que se pueden realizar
        
if __name__ == "__main__":
    while True:
        print("Seleccione una acción:")
        print("1. Insertar")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Ver")
        print("5. Exportar collection a JSON")
        print("6. Salir")
        
        opcion = input("Ingrese el número de la acción que desea realizar: ")
        
        if opcion == "1":
            Insertar()
        elif opcion == "2":
            Modificar()
        elif opcion == "3":
            Eliminar()
        elif opcion == "4":
            Ver()
        elif opcion == "5":
            Exportar()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
