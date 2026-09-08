import sys

def leer_ejemplar(nombre_archivo):
    """
    Lee y decodifica un archivo de texto con el formato del ejemplar de "DeliCiencias".
    
    El esquema posicional esperado es:
    - Línea 1: n (total de pedidos)
    - Línea 2: W (capacidad máxima de la mochila en gramos)
    - Línea 3: V (ganancia meta en pesos)
    - Líneas 4 en adelante: wi vi (peso y ganancia del pedido i, separados por espacio)
    
    Parámetros:
    nombre_archivo (str): El nombre del archivo de texto a leer proporcionado desde consola.
    """
    try:
        # Abrimos el archivo en modo lectura estándar
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            # Decodificación del encabezado
            # Usamos strip() para eliminar saltos de línea (\n) o espacios accidentales
            n = int(lineas[0].strip()) # Total de pedidos
            W = int(lineas[1].strip()) # Capacidad máxima de la mochila
            V = int(lineas[2].strip()) # Ganancia meta
            
            # Decodificación de los pedidos
            pedidos = []
            for i in range(3, 3 + n):
                # split() separa por el delimitador de espacio. 
                # map(int, ...) convierte ambos valores de texto a enteros
                peso, ganancia = map(int, lineas[i].strip().split())
                pedidos.append((peso, ganancia))
                
            # 3. Salida de datos en consola
            print(f"=== DATOS DEL EJEMPLAR ===")
            print(f"Total de pedidos disponibles: {n}")
            print(f"Capacidad máxima de la mochila: {W} gramos")
            print(f"Ganancia meta: ${V} pesos")
            
            # 4. Impresión de ejemplos de pedidos
            print("\n=== PEDIDOS PENDIENTES ===")
            if n >= 2:
                print(f"Pedido 1 -> Peso: {pedidos[0][0]}g, Ganancia: ${pedidos[0][1]}")
                print(f"Pedido 2 -> Peso: {pedidos[1][0]}g, Ganancia: ${pedidos[1][1]}")
            elif n == 1:
                print(f"Único pedido -> Peso: {pedidos[0][0]}g, Ganancia: ${pedidos[0][1]}")
            else:
                print("El catálogo está vacío (0 pedidos).")
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Verifica que el nombre sea correcto.")
    except ValueError:
        print("Error: El archivo contiene caracteres no numéricos o no cumple con el formato esperado.")
    except IndexError:
        print("Error: El archivo tiene menos líneas de las indicadas en el número total de pedidos (n).")

if __name__ == "__main__":
    # Verificamos que el usuario pase exactamente un argumento adicional (el nombre del archivo)
    if len(sys.argv) != 2:
        print("Uso correcto: python programa.py <nombre_del_archivo.txt>")
    else:
        archivo_entrada = sys.argv[1]
        leer_ejemplar(archivo_entrada)