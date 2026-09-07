import sys

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

def guardar_ejemplar(nombre_archivo, pedidos, W, V):
    cadena = optimización_entregas(pedidos, W, V)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(cadena)
    print(f"\n¡Éxito! Archivo '{nombre_archivo}' guardado correctamente.")
    print(f"Cadena binaria generada:\n{cadena}\n")

def crear_archivo():
    print("\n --- CREAR NUEVO EJEMPLAR ---")
    nombre_archivo = input("Nombre del archivo a guardar (ej. ejemplar.txt): ").strip()

    n = pedir_entero("¿Cuántos pedidos deseas ingresar? ", min_val=1)
    pedidos = []
    for i in range(n):
        print(f"Pedido {i+1}:")
        w_i = pedir_entero("Peso (en gramos): ", min_val=0)
        v_i = pedir_entero("Ganancia (en pesos): ", min_val=0)
        pedidos.append((w_i, v_i))
    W = pedir_entero("Capacidad máxima de la mochila W (en gramos): ", min_val=1)
    V = pedir_entero("Ganancia mínima requerida V (en pesos): ", min_val=0)
    guardar_ejemplar(nombre_archivo, pedidos, W, V)
    
def leer_imprimir_ejemplar(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            binarios = f.read().strip()
        n, pedidos, W, V = desbinarizar(binarios)
        print("=== DATOS DEL EJEMPLAR ===")
        print(f"Cantidad de pedidos disponibles: {n}" )
        print(f"Pedidos (peso, ganancia): {pedidos}")
        print(f"Capacidad máxima (W): {W} gramos")
        print(f"Ganancia mínima (V): {V} pesos")
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
        print("1. Crear ejemplar y guardar en archivo")
        print("2. Abrir archivo y mostrar ejemplar")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            abrir_archivo()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.\n")


    

if __name__ == "__main__":
    menu_principal()