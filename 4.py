import os

def crear_listin():
    if not os.path.exists("listin.txt"):
        with open("listin.txt", "w"):
            print("Se ha creado un nuevo listín telefónico.")

def consultar_telefono(nombre):
    with open("listin.txt", "r") as archivo:
        for linea in archivo:
            nombre_cliente, telefono = linea.strip().split(",")
            if nombre_cliente == nombre:
                return telefono
    return "El cliente no se encuentra en el listín telefónico."

def agregar_cliente(nombre, telefono):
    with open("listin.txt", "a") as archivo:
        archivo.write(f"{nombre},{telefono}\n")
    print("Se ha agregado el cliente al listín telefónico.")

def eliminar_cliente(nombre):
    with open("listin.txt", "r") as archivo:
        lineas = archivo.readlines()
    with open("listin.txt", "w") as archivo:
        for linea in lineas:
            nombre_cliente, _ = linea.strip().split(",")
            if nombre_cliente != nombre:
                archivo.write(linea)
    print("Se ha eliminado el cliente del listín telefónico.")

def menu():
    print("\nMenú:")
    print("1. Consultar teléfono de un cliente")
    print("2. Añadir teléfono de un nuevo cliente")
    print("3. Eliminar teléfono de un cliente")
    print("4. Salir")

def main():
    crear_listin()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            print(consultar_telefono(nombre))
        elif opcion == "2":
            nombre = input("Ingrese el nombre del nuevo cliente: ")
            telefono = input("Ingrese el teléfono del nuevo cliente: ")
            agregar_cliente(nombre, telefono)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            eliminar_cliente(nombre)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
