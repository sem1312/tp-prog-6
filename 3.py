while True:
  try:
      n = int(input("Introduce un número entero entre 1 y 10: "))
      m = int(input("Introduce otro número entero entre 1 y 10: "))
      if (n < 1 or n > 10) or (m < 1 or m > 10):
          raise ValueError
      break
  except ValueError:
      print("Por favor, introduce un número entero válido entre 1 y 10.")

nombre_archivo = f"tabla-{n}.txt"

try:
  with open(nombre_archivo, "r") as archivo:
      for i, linea in enumerate(archivo, 1):
          if i == m:
              print("La línea {} del archivo {} es: {}".format(m, nombre_archivo, linea.strip()))
              break
except FileNotFoundError:
  print(f"El archivo {nombre_archivo} no se encuentra.")
