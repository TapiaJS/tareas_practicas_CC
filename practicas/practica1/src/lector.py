import sys

def leer_ejemplar(nombre_archivo):
    try:
        # Abrimos el archivo en modo lectura
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

            # Decodificamos los datos generales del ejemplar eliminando saltos de línea
            n = int(lineas[0].strip())
            W = int(lineas[1].strip())
            V = int(lineas[2].strip())

            # Decodificamos los pedidos
            pedidos = []
            for i in range(3, 3 + n):
                # Separamos el peso y la ganancia por el espacio
                peso, ganancia = map(int, lineas[i].strip().split())
                pedidos.append((peso, ganancia))

        print(f"=== DATOS DEL EJEMPLAR ===")
        print(f"Total de pedidos disponibles: {n}")
        print(f"Capacidad máxima de la mochila: {W}")
        print(f"Ganancia meta: {V}")

        print(f"=== PEDIDOS EN ESPERA ===")
        if n >=2:
            print(f"Pedido 1 -> Peso: {pedidos[0][0]}g, Ganancia: ${pedidos[0][1]}")
            print(f"Pedido 2 -> Peso: {pedidos[1][0]}g, Ganancia: ${pedidos[1][1]}")
        elif n == 1:
            print(f"Ejemplo único -> Peso: {pedidos[0][0]}g, Ganancia: ${pedidos[0][1]}")
        else:
            print("No hay pedidos en el catálogo.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except ValueError:
        print(f"Error: El archivo no cumple con el formato numérico esperado.")

if __name__ == "__main__":
    # Verificamos que el usuario pase el nombre del archivo desde consola
    if len(sys.argv) != 2:
        print("Uso correcto: python lector.py ejemplar1.txt")
    else:
        archivo_entrada = sys.argv[1]
        leer_ejemplar(archivo_entrada)