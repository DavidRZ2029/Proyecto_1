import pygame
import easygui
import pickle
import random
import math

# =====================================================================
# LIFE LIKE - Automata Celular 
# =====================================================================
###### Se va a trabajar con base al trabajo de la clase 13
from random import randint
# =====================================================================
# CODIGO
# =====================================================================
def generar_matriz_aleatorias(filas, columnas):
    """Función que que hace que retorna una matriz 
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def obtener_vecinos(M, f, c):



    """Función quehace retornar retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""



    vecinos = []
    for filas_vecinas in range(f - 1, f + 2):
        for columnas_vecinas in range(c - 1, c + 2):
            if filas_vecinas != f or columnas_vecinas != c:
                filas_vecinas = filas_vecinas % len(M)
                columnas_vecinas = columnas_vecinas % len(M[0])
                vecinos.append(M[filas_vecinas][columnas_vecinas])
    return vecinos








def transicion_celula(estado, vecinos):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos.
    Si estado == 0 y tiene 3 vecinos vivos Entoncess viva
    Si estado == 1 y tiene menos de 2 vecinos vivos Entocess muere
    Si estado == 1 y tiene más de 3 vecinos vivos Entoncesss muere Cualquier otra combinación, el estado sigue igual."""
    
    
    
    
    vivos = sum(vecinos)
    if estado == 0 and vivos == 3:   
        return 1
    if estado == 1 and vivos < 2:    
        return 0
    if estado == 1 and vivos > 3:    
        return 0
    return estado    


def transicion(M):

    """Toma a la matriz  y segun esta completa y le aplica la función de transición a cada célula con su propio vecindario y deja que el resultado en una matriz nueva."""
    filas = len(M)
    columnas = len(M[0])
    nueva = []
    for f in range(filas):
        fila_nueva = []
        for c in range(columnas):
            estado = M[f][c]
            vecinos = obtener_vecinos(M, f, c)
            nuevo_estado = transicion_celula(estado, vecinos)
            fila_nueva.append(nuevo_estado)
        nueva.append(fila_nueva)
    return nueva


tamaño = 20
filas = 75
columnas = 75
tick = 100

def lifelike():
    pygame.init()
    reloj = pygame.time.Clock()
    Matriz = generar_matriz(filas, columnas)
    w, h = columnas * tamaño, filas * tamaño
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    pausa = not pausa
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tamaño
                    c = x // tamaño
                    Matriz[f][c] = (Matriz[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if Matriz[f][c] == 1:
                    x = c * tamaño
                    y = f * tamaño
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tamaño, tamaño))
        if not pausa:
            Matriz = transicion(Matriz)
        pygame.display.update()
        reloj.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()
# =====================================================================
# CODIGO
# =====================================================================


# =====================================================================
# HORMIGA DE LANGTON - Automata Celular
# =====================================================================

hormiga_fila = 0
hormiga_col = 0
hormiga_direccion = 0 # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda

# =====================================================================
# CODIGO
# =====================================================================

#Funcion para generar los colores

#Funcion para generar matriz vacia
def generar_matriz_vacia(filas, columnas):
    """
    crea una matriz llena de ceros.
    El 0 representa el color por defecto (blanco).

    Entradas: 
    - filas: numero de filas (int)
    - columnas: numero de columnas (int)

    Salidas: la matriz de filas x columnas con puros ceros

    Restricciones: filas y columnas deben ser enteros positivos
    """
    if type(filas) != int or filas <= 0:
        raise Exception("El numero de filas debe ser un entero positivo")
    
    if type(columnas) != int or columnas <= 0:
        raise Exception("El numero de columnas debe ser un entero positivo")
    
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

#Funcion para generar matriz aleatoria

#Funcion para cambiar la direccion de la hormiga

#Funcion para mover la hormiga una celda adelante

#Funcion que busca que hacer, y ejecuta las dos funciones pasadas

#Funcion que pide parametros, mediante easygui

#Funcion que dibuja la matriz en la pantalla de pygame

#Funcion que guarda el estado actual del automata, mediante pickle

#Funcion que carga el estado del automata mediante un archivo pickle

#Funcion principal que corre el loop del programa

# =====================================================================
# MENU PRINCIPAL - INTERFAZ
# =====================================================================
def main():
    """
    muestra un menu para que el usuario elija que automata quiere usar.
    Entradas: nada
    Salidas: nada, llama a la funcion del automata elegido
    
    -David Rodríguez Zúñiga
    """
    opciones = [
        "Hormiga de Langton (Generalizada)",
        "Salir"
        
        #Toño aquí agregue la opcion de Life-Like
    ]

    while True:
        eleccion = easygui.buttonbox(
            "Bienvenido al simulador de Automatas Celulares!\n\nElige que automata quieres usar:",
            title="Automatas Celulares",
            choices=opciones
        )

        if eleccion is None or eleccion == "Salir":
            print("Hasta luego!")
            break

        elif eleccion == "Hormiga de Langton (Generalizada)":
            correr_hormiga()
            
        #Agregue el elif para el life like y la funcion de correr_lifelike()


if __name__ == "__main__":
    main()
