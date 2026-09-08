import sys
import heapq


BITS = 16

def pedir_entero(mensaje, min_val=0):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < min_val:
                print(f"[Error] El número no puede ser menor a {min_val}. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("[Error] Entrada inválida. Por favor, ingresa un número entero.")

def binarizar(decimal, bits=BITS):
    return bin(decimal)[2:].zfill(bits)

def optimización_entregas(pedidos, W, V, bits=BITS):
    cadena_binaria = ""
    for w_i, v_i in pedidos:
        cadena_binaria += binarizar(w_i, bits)
        cadena_binaria += binarizar(v_i, bits)
    cadena_binaria += binarizar(W, bits)
    cadena_binaria += binarizar(V, bits)

    return cadena_binaria

def desbinarizar(binarios, bits=BITS):
    if len(binarios) < bits * 2 or len(binarios) % bits != 0:
        raise ValueError("La cadena binaria no tiene un formato o lóngitud válida.")

    bits_pedidos = binarios[:-2 * bits]
    bits_W = binarios[-2 * bits : -bits]
    bits_V = binarios[-bits:]

    W = int(bits_W,2)
    V = int(bits_V,2)
    pedidos = []
    tamano_tupla = 2 * bits
    contador = 0

    for i in range(0, len(bits_pedidos), tamano_tupla):
        bloque_w = bits_pedidos[i : i + bits]
        bloque_v = bits_pedidos[i + bits : i + tamano_tupla]
        w_i = int(bloque_w,2)
        v_i = int(bloque_v,2)
        pedidos.append((w_i, v_i))

    contador = len(pedidos)

    return contador, pedidos, W, V



def comprobar_pesos(binarios, bits = BITS):
    # Se comprueban los pesos de cada pedido
    # En caso de no cumplirlo no puede ejecutar el algoritmo, ya que se pide extrictamente que sean de pesos iguales
    # Comprobar que los bits de las tuplas para cada pedido sean iguales,
    # tomar la muestra de uno y comparalo con los demas

    contador, pedidos, W, V = desbinarizar(binarios, bits=BITS)

    maxsum = 0
    maxweight = 0

    #comprobamos que existan pedidos
    if not pedidos:
        return 0, 0

    #Iteramos para saber si el valor de cada pedido es el optimo para V sin rebasar W
    for i in range(1, len(pedidos)):
        if pedidos[i][0] != pedidos[i-1][0]:
            return 0, 0
        maxsum += pedidos[i-1][1]
        maxweight += pedidos[i-1][0]
    #Caso cuando el peso de la mochila no es rebasado y el valor total de todos los pedidos es igua a V
    if maxweight <= W and maxsum >= V:
        return 1, maxweight
    #reiniciamos a 0 la suma maxima de maxweight
    maxweight = 0
    maxsum = 0
    #Generamos un Max-Heap para extrar los m elementos mayores para el alcanzar el valor V
    # Invertimos los pesos de las tuplas para empezar con los valores mayores
    max_heap = [(-ganancia, peso) for peso, ganancia in pedidos]
    heapq.heapify(max_heap)
    
    for i in range(len(pedidos)):
        # Extraemos la tupla (-valor, peso) del Max-Heap en una variable
        pedido_actual = heapq.heappop(max_heap)
        print("pedido actual:", pedido_actual)
        print("maxweight:", maxweight, " maxsum:", maxsum)

        if maxweight + pedido_actual[1] <= W and maxsum + abs(pedido_actual[0]) >= V:
            maxweight += pedido_actual[1]
            maxsum += abs(pedido_actual[0])
            return 1, maxweight

        elif maxweight + pedido_actual[1] <= W:
            maxweight += pedido_actual[1]
            maxsum += abs(pedido_actual[0])
        else:
            # Se rebaso el peso de la mochila y no se puede alcanzar el valor V
            # No se rebasa el peso de la mochila pero V no es alcanzado
            # Se rebaso el peso de la mochila pero si es posible alcanzar V
            return 0, maxweight

    return 0, 0
    # Comprobar que el peso de la primera mochila no sobrepasa W, si es asi, entonces no es posible el valor V
    # Utilizar algoritmo gready para poder saber el valor maximo de cada pedido, 
    # si es que no se alcanza V, el siguiente valor se suma.
    # Para ordenar los valores y mantener una suma de los valores mas altos se ordena en un Max-heap.
    # esto toma O(nlog(m)), iterar O(n), decodificar O(n).  O(nlog(m)) tomaria el resultado, siempre que m <= n 

# Imprime la respuesta del programa solicitado
def respuesta(resultado):
    if resultado[0] == 1:
         print("SI\n")
         print("Peso total:", resultado[1])
    else:
        print("NO")


def leer_imprimir_ejemplar(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            binarios = f.read().strip()
        n, pedidos, W, V = desbinarizar(binarios)
        res = comprobar_pesos(binarios, W)
        respuesta(res)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.\n")
    except ValueError as e:
        print(f"{e}\n")

def abrir_archivo():
    print("\n --- LECTURA DE ARCHIVO ---")
    nombre_archivo = input("Ingrese el nombre del archivo a abrir: ").strip()
    leer_imprimir_ejemplar(nombre_archivo)

def menu_principal():
    while True:
        print("=" * 10)
        print(" SISTEMA DE ENTREGAS DELICIENCIAS ")
        print("=" * 10)
        print("1. Abrir archivo y mostrar ejemplar")
        print("2. Salir")

        opcion = input("Selecciona una opción (1-2): ").strip()

        if opcion == "1":
            abrir_archivo()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.\n")

if __name__ == "__main__":
    menu_principal()

