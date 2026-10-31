# README - Práctica 2: Compejidad Computacional

Este proyecto contiene la implementación de un generador de ejemplares, certificados y un verificador para el "Problema de la Mochila" del caso de estudio de "Deliciencias".

## Requisitos Previos.

* **Lenguaje:** Python 3.x. Dado que Python es un lenaguaje interpretado, no se requiere un paso previo de compilación.

* **Dependencias:** Ninguna. Todo el código fue desarrollado utilizando únicamente las biliotecas estándar de Python.

## Instrucciones de Ejecución
**Nota importante:** Deberás de tener la terminal abierta ubicada en la ubicación del programa que se desea ejecutar, de igual manera, deberás de colocar los archivos que desees trabajar ahí mismo.
Por ejemplo, si se busca trabajar el archivo Generador_Certificados.py Se deben de colocar los archivos que se desean procesar en esa ubicación, abrir la terminal en esa ubicación y seguir los pasos mostrados en la terminal para su correcta ejecución.


### Preludio:
Debido a que pedían ejemplares "grandes" se creó un programa que generá ejemplares aleatorios, para cumplir con ese apartado. Se encuentra en la carpeta: 0_Generador_Ejemplares. Donde contiene el programa Generador_Ejemplares.py. Este programa genera 3 ejemplares aleatorios. Todo es al azar, W, V y las tuplas v_i, w_i. Modificado de cierta manera, para que probabilísticamente se generen ejemplares que sean válidos. Modificando los rangos de probabilidad de las variables.
(La carpeta 01_Imprimir_Codificaciones, contiene el archivo de la práctica 1, por si desea ver de mejor manera, los archivos generados, pues se siguen generando en binario).

### Ejercicio 2:
Carpeta 1_Generador_Certificados, contiene Generador_Certificados.py. En esa carpeta deberá colocar los ejemplares que desea generar su certificado. Tiene un 25% de probabilidad de tomar un pedido. 

### Ejercicio 3:
Carpeta 2_Verificador, contiene Verificador.py. Deberás de colocar el ejemplar y los certificados asociados a ese ejemplar. 

Los ejemplares y certificados usados se encuentran en sus respectivas carpetas. El nombre de cada certificado, si tiene V es válido, F inválido, con una pequeña descripción de lo que se hizó.