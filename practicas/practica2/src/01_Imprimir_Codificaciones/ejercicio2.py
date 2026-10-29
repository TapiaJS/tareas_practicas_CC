import sys

BITS = 16

def pedir_entero(mensaje, min_val=0):
    """
    Pide una entrada al usuario y comrpueba que sea un número entero válido
    mayor o igual al valor mpinimo especificado.

    :param mensaje: El texto que se le mostrará al usuario en consola.
    :param min_val: El valor mínimo permitido para la entrada (por defecto 0).
    :return: El número entero válido ingresado por el usuario.

    """
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
    """
    Convierte a binario el decimal otorgado y crea el bloque de bits para el número.

    :param decimal: El decimal a transformar a binario.
    :param bits: La cantidad de bits asignada para representar cada número binario.
    :return: Una cadena de texto (string) que representa el número en binario. 

    """
    return bin(decimal)[2:].zfill(bits)

def optimización_entregas(pedidos, W, V, bits=BITS):
    """
    
    Recibe los elementos del problema de entregas y los codifica en una sola cadena binaria..

    :param pedidos: Lista de tuplas, donde cada una contiene (peso wi, valor vi) de un pedido.
    ;param W: La capacidad máxima de peso de la mochila.
    :param V: La meta mínima de ganancias a cumplir.
    :bits: La cantidad de bits asignada para representar cada número binario.
    :return: Una cadena de texto (string) que contiene todos los datos concatenados en binario.

    """
    cadena_binaria = ""
    for w_i, v_i in pedidos:
        cadena_binaria += binarizar(w_i, bits)
        cadena_binaria += binarizar(v_i, bits)
    cadena_binaria += binarizar(W, bits)
    cadena_binaria += binarizar(V, bits)

    return cadena_binaria

def desbinarizar(binarios, bits=BITS):
    """
    Decodifica una cadena binaria para reconstruir los datos originales del problema de optimización.

    :param binarios: La cadena de texto binaria que contiene toda la información empaquetada.
    :param bits: La cantidad de bits asignada para representar cada número binario.
    :return: Una tupla con (contador de pedidos, lista de pedidos, peso W, ganancia V).
    :raises ValueError: Si la longitud de la cadena binaria no es válida o es menor al mínimo requerido.

    """
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
    """
    Convierte la instancia del problema a su representación binaria y la guarda en un archivo de texto.

    :param nombre_archivo: Nombre del archivo donde se almacenará la información.
    :param pedidos: Lista de tuplas (w_i, v_i) con el peso y valor de cada pedido.
    ;param W: La capacidad máxima de peso de la mochila.
    :param V: La meta mínima de ganancias a cumplir.

    """
    cadena = optimización_entregas(pedidos, W, V)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(cadena)
    print(f"\n¡Éxito! Archivo '{nombre_archivo}' guardado correctamente.")
    print(f"Cadena binaria generada:\n{cadena}\n")

def crear_archivo():
    """
    Interactúa con el usuario desde la consola para capturar los datos de un ejemplar del problema
    Con cuantos pedidos creará, (lista de pedidos con peso / ganancia, capacidad W y ganancia mínima V)
    de forma validada, solicitando posteriormente su almacenamiento en disco mediante la función guardar_ejemplar.
    """
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
    """
    Lee un archivo codificado en binario, procesa sus datos a través de la función
    desbinarizar e imprime en la consola la información reconstruida del ejemplar
    (pedidos, capacidad W y ganancia V), gestionando errores de lectura o formato.

    :param nombre_archivo: Nombre del archivo que contiene la cadena binaria.
    
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            binarios = f.read().strip()
        n, pedidos, W, V = desbinarizar(binarios)
        print("=== DATOS DEL EJEMPLAR ===")
        print(f"Cantidad de pedidos disponibles: {n}" )
        print(f"Pedidos (peso, ganancia): {pedidos}")
        print(f"Capacidad máxima (W): {W} gramos")
        print(f"Ganancia mínima (V): {V} pesos")

        print("\nEjemplos de pedidos disponibles: ")
        if n >= 1:
            print(f"  - Pedido 1: Peso = {pedidos[0][0]} g, Ganancia = ${pedidos[0][1]}")
        if n >= 2:
            print(f"  - Pedido 2: Peso = {pedidos[1][0]} g, Ganancia = ${pedidos[1][1]}")
        elif n < 1:
            print(" - No hay pedidos registrados en el ejemplar.")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.\n")
    except ValueError as e:
        print(f"{e}\n")

def abrir_archivo():
    """
    
    Solicita al usuario el nombre del archivo de entrada mediante la consola
    y ejecuta la lectura e impresión de los datos llamando a leer_imprimir_ejemplar.

    """
    print("\n --- LECTURA DE ARCHIVO ---")
    nombre_archivo = input("Ingrese el nombre del archivo a abrir: ").strip()
    leer_imprimir_ejemplar(nombre_archivo)

def menu_principal():
    """
    Despliega el menú interactivo principal en consola que coordina las acciones del programa:
    creación de nuevos ejemplares, lecturas de archivos guardados y salir del programa.
    
    """
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