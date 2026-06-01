import pygame
import easygui
import pickle
import random
import math

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