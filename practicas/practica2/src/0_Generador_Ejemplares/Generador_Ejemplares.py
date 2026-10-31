import random
import sys

BITS = 16
VALOR_MAX_VW = (2**BITS) - 1 #Valor máximo representable: 65535.
VALOR_MAX_WVI = VALOR_MAX_VW // 15

def binarizar(decimal, bits=BITS):
    """
    Convierte a binario el decimal otorgado y crea el bloque de birs para el número.
    """
    return bin(decimal)[2:].zfill(bits)

def generar_cadena_ejemplar():
    """
    Genera los pedidos siguiendo la gramática:
    S -> (E) A A
    E -> (valor, valor), E | epsilon
    A -> valor numérico <= 65535

    La regla E tiene un 5% de proabilidad de derivar en epsilon (detenerse).
    """
    pedidos = []
    while True:
        #Probabilidad de terminar la secuencia de pedidos.
        if random.random() < 0.02 and len(pedidos) > 0:
            break
        #Generación para los valores de los pedidos.
        w_i = random.randint(1, VALOR_MAX_WVI)
        v_i = random.randint(1, VALOR_MAX_WVI)
        pedidos.append((w_i, v_i))

    #Generación de la capacidad y ganancia.
    W = random.randint(VALOR_MAX_WVI, VALOR_MAX_VW)
    V = random.randint(1, VALOR_MAX_VW)

    #Codificación binaria.
    cadena_binaria = ""
    for w_i,  v_i in pedidos:
        cadena_binaria += binarizar(w_i, BITS)
        cadena_binaria += binarizar(v_i, BITS)

    cadena_binaria += binarizar(W, BITS)
    cadena_binaria += binarizar(V, BITS)
    return cadena_binaria, pedidos, W, V

def generador_ejemplares_aleatorios(nombre_archivo):
    """
    Genera un ejemplar aleatorio largo respetando la gramática y lo almacena en un archivo.
    """
    cadena, pedidos, W, V = generar_cadena_ejemplar()
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(cadena)

    print(f"--- EJEMPLAR GENERADO EXITOSAMENTE ---")
    print(f"Archivo guardado: {nombre_archivo}")
    print(f"Cantidad de pedidos creados: {len(pedidos)}")
    print(f"Capacidad máxima (W): {W} | Ganancia meta (V): {V}")
    print(f"Longitud total de la cadena binaria: {len(cadena)} bits")
    print(f"Muestra inicial de la cadena:\n{cadena[:64]}...")

if __name__ == "__main__":
    for i in range(3):
        archivo_salida = (sys.argv[1] if len(sys.argv) > 1 else f"ejemplar_aleatorio{i}.txt")
        generador_ejemplares_aleatorios(archivo_salida)