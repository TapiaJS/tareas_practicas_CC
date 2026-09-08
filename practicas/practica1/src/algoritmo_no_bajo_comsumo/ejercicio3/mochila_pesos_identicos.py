import sys

def resolver_pesos_identicos(nombre_archivo):
    """
    Algoritmo eficiente para resolver el Problema de la Mochila 0/1 
    cuando todos los pesos son idénticos.
    
    Parámetros:
    nombre_archivo (str): Ruta del archivo de texto con el ejemplar.
    """
    try:
        # LECTURA Y DECODIFICACIÓN (Reutilizando lógica del Ejercicio 2)
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            n = int(lineas[0].strip()) # Total de pedidos
            W = int(lineas[1].strip()) # Capacidad máxima de la mochila
            V = int(lineas[2].strip()) # Ganancia meta
            
            # Si el catálogo está vacío, es imposible alcanzar una ganancia mayor a 0
            if n == 0:
                if V <= 0:
                    print("SÍ\n0")
                else:
                    print("NO")
                return

            ganancias = []
            peso_constante = 0
            
            # Extraemos las ganancias y determinamos el peso constante
            for i in range(3, 3 + n):
                peso, ganancia = map(int, lineas[i].strip().split())
                ganancias.append(ganancia)
                # Tomamos el peso del primer pedido como el peso constante para todos
                if i == 3:
                    peso_constante = peso

        # ALGORITMO EFICIENTE (Greedy / Ordenamiento)
        
        # Evitamos división por cero en caso de que el peso sea 0
        if peso_constante > 0:
            # Calculamos cuántos pedidos caben físicamente en la mochila
            k = W // peso_constante 
        else:
            k = n
            
        # El límite real de paquetes a llevar es el mínimo entre lo que cabe (k) y lo que existe (n)
        k = min(k, n)
        
        # Ordenamos las ganancias de mayor a menor. 
        # Esta es la operación dominante y nos da la complejidad de O(n log n).
        ganancias.sort(reverse=True)
        
        # Sumamos las 'k' mejores ganancias posibles
        ganancia_maxima = sum(ganancias[:k])
        
        # EVALUACIÓN Y SALIDA 
        if ganancia_maxima >= V:
            print("SÍ")
            peso_total = k * peso_constante
            print(peso_total)
        else:
            print("NO")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except ValueError:
        print("Error: Formato de archivo inválido.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso correcto: python mochila_pesos_identicos.py <nombre_del_archivo.txt>")
    else:
        archivo_entrada = sys.argv[1]
        resolver_pesos_identicos(archivo_entrada)