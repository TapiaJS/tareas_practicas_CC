import sys

BITS = 16

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
        contador += 1
        bloque_w = bits_pedidos[i : i + bits]
        bloque_v = bits_pedidos[i + bits : i + tamano_tupla]
        w_i = int(bloque_w,2)
        v_i = int(bloque_v,2)
        pedidos.append((w_i, v_i))

    return contador, pedidos, W, V

def guardar_ejemplar(nombre_archivo, pedidos, W, V):
    cadena = optimización_entregas(pedidos, W, V)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(cadena)

def leer_imprimir_ejemplar(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        binarios = f.read().strip()
    n, pedidos, W, V = desbinarizar(binarios)
    print("=== DATOS DEL EJEMPLAR ===")
    print(f"Cantidad de pedidos disponibles: {n}" )
    print(f"Pedidos (peso, ganancia): {pedidos}")
    print(f"Capacidad máxima (W): {W} gramos")
    print(f"Capacidad mínima (V): {V} pesos")


    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
    else:
        archivo = input("Ingrese el nombre del archivo de entrada: ").strip()
    try:
        leer_imprimir_ejemplar(archivo)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe. Creando uno de prueba...")
        guardar_ejemplar(archivo, [(1,2), (0,3), (4,5), (4,5)], 10, 5)
        print("Archivo creado exitosamente. Leyendo de nuevo:\n")
        leer_imprimir_ejemplar(archivo)