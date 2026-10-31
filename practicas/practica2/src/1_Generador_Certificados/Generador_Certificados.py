import os
import random
import sys

BITS = 16

def desbinarizar_ejemplar(binarios, bits=BITS):
    """
    Decodifica la cadena binaria del ejemplar para extraer pedidos, W y V.
    """
    if len(binarios) < bits * 2 or len(binarios) % bits != 0:
        raise ValueError("La cadena binaria del ejemplar no tiene un formato o longitud válida.")

    bits_pedidos = binarios[:-2 * bits]
    bits_W = binarios[-2 * bits : -bits]
    bits_V = binarios[-bits:]

    W = int(bits_W, 2)
    V = int(bits_V, 2)

    pedidos = []
    tam_tupla = 2 * bits

    for i in range(0, len(bits_pedidos), tam_tupla):
        bloque_w = bits_pedidos[i : i + bits]
        bloque_v = bits_pedidos[i + bits : i + tam_tupla]
        w_i = int(bloque_w, 2)
        v_i = int(bloque_v, 2)
        pedidos.append((w_i, v_i))

    return pedidos, W, V

def generar_certificado_aleatorio(num_pedidos, prob_tomar=0.25):
    """
    Genera un arreglo de 0's y 1's asignando 1 con una probabilidad de prob_tomar. 
    Por defecto del 25%.
    """
    return [1 if random.random() < prob_tomar else 0 for _ in range(num_pedidos)]

def crear_certificado():
    nombre_ejemplar = input("Ingrese el nombre del archivo del ejemplar: ").strip()

    if not os.path.exists(nombre_ejemplar):
        print(f"[Error] El archivo '{nombre_ejemplar}' no existe.")
        return

    try:
        with open(nombre_ejemplar, "r", encoding="utf-8") as f:
            binarios = f.read().strip()

        pedidos, W, V = desbinarizar_ejemplar(binarios)
        n_pedidos = len(pedidos)
        certificado_arreglo = generar_certificado_aleatorio(n_pedidos)
        certificado_binario = "".join(map(str, certificado_arreglo))
        nombre_salida = input("Ingrese el nombre para guardar el certificado (ej. certificado.txt): ").strip()
        if not nombre_salida:
            nombre_salida = "certificado.txt"
        with open(nombre_salida, "w", encoding="utf-8") as f:
            f.write(certificado_binario)

        # Confirmación limpia en consola
        print("\n" + "=" * 55)
        print("         ¡CERTIFICADO GENERADO CON ÉXITO!         ")
        print("=" * 55)
        print(f"Archivo del Ejemplar (Entrada) : {nombre_ejemplar}")
        print(f"Archivo del Certificado (Salida): {nombre_salida}")
        print(f"Total de pedidos evaluados     : {n_pedidos}")
        print(f"Longitud de la cadena generada : {len(certificado_binario)} bits")
        print(f"Cadena del certificado         : {certificado_binario}")
        print("=" * 55 + "\n")

        return nombre_salida
    except Exception as e:
        print(f"[Error al procesar el ejemplar]: {e}")


if __name__ == '__main__':
    crear_certificado()