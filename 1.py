while True:
    try:
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        if numero < 1 or numero > 10:
            raise ValueError
        break
    except ValueError:
        print("Por favor, introduce un número entero válido entre 1 y 10.")

nombre_archivo = f"tabla-{numero}.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(f"Tabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        archivo.write(f"{resultado}\n")
