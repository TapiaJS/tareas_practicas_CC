import os
import sys

BITS = 16

def desbinarizar_ejemplar(binarios, bits=BITS):
    """
    Decodifica la cadena binaria del ejemplar para extraer pedidos, W y V.
    """
    if len(binarios) < bits * 2 or len(binarios) % bits != 0:
        raise ValueError("La cadena binaria del ejemplar no tiene un formato válido.")
    bits_pedidos = binarios[:-2 * bits]
    bits_W = binarios[-2 * bits: -bits]
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

def verificar_certificado():
    if len(sys.argv) >=3:
        nombre_ejemplar = sys.argv[1]
        nombre_certificado = sys.argv[2]
    else:
        print("--- ALGORITMO DE VERIFICACIÓN ---")
        nombre_ejemplar = input("Ingrese el nombre del archivo del EJEMPLAR: ").strip()
        nombre_certificado = input("Ingrese el nombre del archivo del CERTIFICADO: ").strip()

    if not os.path.exists(nombre_ejemplar):
        print(f"[ERROR] No existe el archivo del ejemplar: '{nombre_ejemplar}'")
        return
    if not os.path.exists(nombre_certificado): 
        print(f"[ERROR] No existe el archivo del certificado: '{nombre_certificado}'")
        return

    try:
        with open(nombre_ejemplar, "r", encoding="utf-8") as f:
            binario_ejemplar = f.read().strip()

        with open(nombre_certificado, "r", encoding="utf-8") as f:
            cadena_certificado = f.read().strip()

        pedidos, W, V = desbinarizar_ejemplar(binario_ejemplar)
        n_pedidos = len(pedidos)

        print("\n" + "=" * 60)
        print("          RESULTADO DE LA VERIFICACIÓN DE CERTIFICADO         ")
        print("=" * 60)
        print(f"Ejemplar analizado    : {nombre_ejemplar}")
        print(f"Certificado analizado : {nombre_certificado}")
        print(f"Capacidad máxima (W)  : {W} gramos")
        print(f"Ganancia meta (V)     : {V} pesos")
        print(f"Total pedidos ejemplar: {n_pedidos}")
        print(f"Longitud certificado  : {len(cadena_certificado)} bits")
        print("-" * 60)

        #Comprueba que la longitud del certificado y de tuplas sean iguales.
        if len(cadena_certificado) != n_pedidos:
            print("[RECHAZADO] Error de Estructura/Formato:")
            print(f"  -> El certificado tiene {len(cadena_certificado)} bits, pero el ejemplar requiere {n_pedidos} bits.")
            print("\n¿Satisface la condición de pertenencia al lenguaje? NO")
            print("=" * 60)
            return

        #Recorrido en paralelo e inspección elemento por elemento.
        peso_acumulado = 0
        ganancia_acumulada = 0
        elementos_tomados = 0
        exceso_detectado = False
        print("Detalle del recorrido en paralelo:")
        for i in range(n_pedidos):
            bit = cadena_certificado[i]
            w_i, v_i = pedidos[i]

            if bit == '1':
                peso_acumulado += w_i
                ganancia_acumulada += v_i
                elementos_tomados += 1
                print( f" [Bit {i+1}: 1] Toma Pedido {i+1} ({w_i}g, ${v_i}) -> Acumulado: {peso_acumulado}g, ${ganancia_acumulada}.")

                if peso_acumulado > W:
                    print(f"\n[CORTE TEMPRANO Exceso de capacidad en el pedido {i+1:}")
                    print(f"  -> Peso acumulado ({peso_acumulado}g) supera el límite máximo de la mochila ({W}g).")
                    exceso_detectado = True
                    break
            elif bit == '0':
                print(f"  [Bit {i+1}: 0] Omite Pedido {i+1}")
            else:
                print(f"\n[RECHAZADO] Bit no válido '{bit}' encontrado en la posición {i+1}.")
                print("\n¿Satisface la condición de pertenencia al lenguaje? NO")
                print("=" * 60)
                return
            print("-" * 60)
        print("RESUMEN DE EVALUACIÓN:")
        print(f"  - Pedidos seleccionados : {elementos_tomados} de {n_pedidos}")
        print(f"  - Peso acumulado total  : {peso_acumulado} / {W} g")
        print(f"  - Ganancia acumulada    : ${ganancia_acumulada} / ${V}")

        # PASO 3: Decisión final de pertenencia al lenguaje
        if exceso_detectado:
            pertenece = False
            razon = "El peso total excede la capacidad de la mochila."
        elif peso_acumulado <= W and ganancia_acumulada >= V:
            pertenece = True
            razon = "El certificado cumple el límite de peso Y alcanza/supera la ganancia meta."
        else:
            pertenece = False
            razon = f"La ganancia acumulada (${ganancia_acumulada}) no alcanza la meta solicitada (${V})."

        print("-" * 60)
        if pertenece:
            print("RESPUESTA FINAL: SÍ (El certificado ES VÁLIDO)")
        else:
            print("RESPUESTA FINAL: NO (El certificado ES INVÁLIDO)")
        print(f"Motivo: {razon}")
        print("=" * 60 + "\n")

    except Exception as e:
        print(f"\n[Error durante la verificación]: {e}\n")


if __name__ == "__main__":
    verificar_certificado()