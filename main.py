from pymongo import MongoClient
import json
from bson import json_util  # Importa json_util para manejar ObjectId

# Conectarse a la base de datos local de MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Seleccionar una base de datos (si no existe, se creará automáticamente)
db = client['mydatabase']

# Crear una colección llamada 'mycollection'
collection = db['tareas']

# Leer los datos del archivo JSON
with open('database.json', 'r') as file:
    data = json.load(file)

# Verificar si la colección está vacía
if collection.count_documents({}) == 0:
    # La colección está vacía, cargar los datos del archivo JSON
    collection.insert_many(data)
    print('Datos cargados desde el archivo JSON.')
else:
    # La colección no está vacía, verificar duplicados antes de insertar
    for document in data:
        # Verificar si la ID del documento ya existe en la colección
        if collection.count_documents({'_id': document['_id']}) == 0:
            # La ID no existe en la colección, insertar el documento
            collection.insert_one(document)
    print('Datos cargados desde el archivo JSON sin duplicados.')

# Insertar un documento en la colección
def Insertar ():
    tarea = input("Ingrese la tarea: ")
    encargado = input("Ingrese el encargado: ")
    fecha = input("Ingrese la fecha (en formato YYYY-MM-DD): ")
    estado = input("Ingrese el estado (pendiente, en proceso, realizado, etc.): ")

    post = {'tarea': tarea, 'encargado': encargado, 'fecha': fecha, 'estado': estado}
    collection.insert_one(post)
    print('----Documento insertado exitosamente----')


# Modificar un documento en la colección
def Modificar():
    tarea_a_modificar = input("Ingrese la tarea que desea modificar: ")

    # Buscar el documento a modificar
    query = {'tarea': tarea_a_modificar}
    documento_a_modificar = collection.find_one(query)

    if documento_a_modificar:
        # Solicitar nuevos valores para cada atributo
        nueva_tarea = input(f"Ingrese la nueva tarea (anterior: {documento_a_modificar['tarea']}): ")
        nuevo_encargado = input(f"Ingrese el nuevo encargado (anterior: {documento_a_modificar['encargado']}): ")
        nueva_fecha = input(f"Ingrese la nueva fecha (anterior: {documento_a_modificar['fecha']}): ")
        nuevo_estado = input(f"Ingrese el nuevo estado (anterior: {documento_a_modificar['estado']}): ")

        # Crear el diccionario con los nuevos valores
        nuevos_valores = {
            'tarea': nueva_tarea,
            'encargado': nuevo_encargado,
            'fecha': nueva_fecha,
            'estado': nuevo_estado
        }

        # Realizar la actualización del documento
        update_result = collection.update_one(query, {'$set': nuevos_valores})

        if update_result.modified_count > 0:
            print('----Documento modificado exitosamente----')
        else:
            print('No se encontró ningún documento para modificar.')
    else:
        print('No se encontró ningún documento con la tarea especificada.')


# Eliminar un documento de la colección
def Eliminar():
    tarea_a_eliminar = input("Ingrese la tarea que desea eliminar: ")

    # Buscar el documento a eliminar
    query = {'tarea': tarea_a_eliminar}
    documento_a_eliminar = collection.find_one(query)

    if documento_a_eliminar:
        # Eliminar el documento
        delete_result = collection.delete_one(query)

        if delete_result.deleted_count > 0:
            print('----Documento eliminado exitosamente----')
        else:
            print('No se pudo eliminar el documento.')
    else:
        print('No se encontró ningún documento con la tarea especificada.')


# Mostrar todos los documentos en la colección
def Ver ():
    print()
    for post in collection.find():
        print(post)
        print()


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