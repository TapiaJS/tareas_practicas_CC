# README - Práctica 1: Complejidad Computacional

Este proyecto contiene la implementación de los algoritmos diseñados para resolver el "Problema de la Mochila 0/1" aplicado al caso de estudio de "DeliCiencias", tanto para formatos de texto plano como para esquemas de codificación de bajo consumo de datos.

## Requisitos Previos

* **Lenguaje:** Python 3.x. Dado que Python es un lenguaje interpretado, no se requiere un paso previo de compilación.

* **Dependencias:** Ninguna. Todo el código fue desarrollado utilizando únicamente las bibliotecas estándar de Python, cumpliendo con la restricción de no utilizar herramientas externas para procesar formatos predefinidos como JSON o CSV.

## Instrucciones de Ejecución

**Nota importante:** Todos los comandos asumen que tienes tu terminal o consola abierta estando ubicado dentro de la carpeta raíz src/.

### 1. Algoritmos de formato de texto (No bajo consumo)

#### Ejercicio 2: Lector de Ejemplares

Este script lee el esquema posicional de texto e imprime en consola los datos generales y dos ejemplos de los pedidos.

Para ejecutar la prueba con `ejemplar1.txt`:


```bash
python algoritmo_no_bajo_comsumo/ejercicio2/lector.py algoritmo_no_bajo_comsumo/ejercicio2/ejemplar1.txt
```

#### Ejercicio 3: Algoritmo Eficiente (Pesos Idénticos)

Este programa evalúa el escenario donde todos los pedidos tienen el mismo peso. Imprime como salida estricta un "SÍ" o "NO" y, en caso afirmativo, el peso total de los paquetes seleccionados.

Para ejecutar el ejemplar donde la respuesta es "SÍ":

```bash
python algoritmo_no_bajo_comsumo/ejercicio3/mochila_pesos_identicos.py algoritmo_no_bajo_comsumo/ejercicio3/ejemplar_si.txt
```

Para ejecutar el ejemplar donde la respuesta es "NO":

```Bash
python algoritmo_no_bajo_comsumo/ejercicio3/mochila_pesos_identicos.py algoritmo_no_bajo_comsumo/ejercicio3/ejemplar_no.txt
```

### 2. Algoritmos de bajo consumo (Esquema estrictamente binario)

Esta sección corresponde a los archivos que procesan el esquema binario de cadenas de '0' y '1', requeridos para simular terminales móviles.

#### Decodificador Binario

Para decodificar e imprimir los datos de un ejemplar en formato binario:

```bash
python algoritmo_bajo_consumo/ejercicio2/ejercicio2.py algoritmo_bajo_consumo/ejercicio2/ejemplar1.txt
```

#### Algoritmo Eficiente Binario (Pesos Idénticos)

Para ejecutar la evaluación sobre el ejemplar codificado en binario donde la respuesta es "SÍ":

```bash
python algoritmo_bajo_consumo/ejercicio3/ejercicio3.py algoritmo_bajo_consumo/ejercicio3/ejemplar3_si
```

Para ejecutar la evaluación sobre el ejemplar codificado en binario donde la respuesta es "NO":

```bash
python algoritmo_bajo_consumo/ejercicio3/ejercicio3.py algoritmo_bajo_consumo/ejercicio3/ejemplar2_no
```