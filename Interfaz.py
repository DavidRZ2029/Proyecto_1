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


# =====================================================================
# CODIGO
# =====================================================================
def likelife():
    filas, columnas, tamaño, birth, survival = pedir_parametros()
 
    pygame.init()
    reloj  = pygame.time.Clock()
    M      = generar_matriz_aleatoria(filas, columnas)
    window = pygame.display.set_mode((columnas * tamaño, filas * tamaño))
    pygame.display.set_caption("Life-Like Automaton")
 
    loop  = True
    pausa = False
 
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:#Pausa
                    pausa = not pausa
                if event.key == pygame.K_g:              # Guardar
                    guardar(M, filas, columnas, tamaño, birth, survival)
                if event.key == pygame.K_c:#Cargar
                    resultado = cargar()
                    if resultado:
                        M, filas, columnas, tamaño, birth, survival = resultado
                        window = pygame.display.set_mode((columnas * tamaño, filas * tamaño))
                if event.key == pygame.K_r:#Reiniciar aleatorio
                    M = generar_matriz_aleatoria(filas, columnas)
                if event.key == pygame.K_b:# Reiniciar con mariz vaciaaa
                    M = generar_matriz_vacia(filas, columnas)
 
            if event.type == pygame.MOUSEBUTTONDOWN:# Clic: cambiar celda
                x, y = pygame.mouse.get_pos()
                f, c = y // tamaño, x // tamaño
                if 0 <= f < filas and 0 <= c < columnas:
                    M[f][c] = (M[f][c] + 1) % 2
 
        dibujar(window, M, tamaño)
        if not pausa:
            M = transicion(M, birth, survival)
        pygame.display.update()
        reloj.tick(10)
 
    pygame.quit()

# =====================================================================
# HORMIGA DE LANGTON - Automata Celular
# =====================================================================

hormiga_fila = 0
hormiga_col = 0
hormiga_direccion = 0 # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda

# =====================================================================
# CODIGO
# =====================================================================

def generar_colores(n):
    """
    genera una lista de n colores distintos en formato RGB.
    El primero siempre es blanco (fondo) y el ultimo siempre es negro,
    los del medio son colores aleatorios para que se vean bonitos.
 
    Entradas:
    - n: cantidad de colores que necesitamos (int), tiene que ser >= 2
 
    Salidas:
    - lista de tuplas RGB, ejemplo: [(255,255,255), (255,0,0), (0,0,0)]
 
    Restricciones: n tiene que ser entero mayor o igual a 2
    """
    if n < 2:
        raise Exception("Necesitas al menos 2 colores (blanco y negro)")
 
    colores = []
    colores.append((255, 255, 255))  # el primer color siempre es blanco
 
    # generamos colores del medio de forma aleatoria
    for i in range(n - 2):
        r = random.randint(50, 200)
        g = random.randint(50, 200)
        b = random.randint(50, 200)
        colores.append((r, g, b))
 
    colores.append((0, 0, 0))  # el ultimo siempre es negro
 
    # caso especial: si solo son 2 colores, ya quedo (blanco y negro)
    return colores

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

def generar_matriz_aleatoria(filas, columnas, num_colores):
    """
    crea una matriz con valores aleatorios entre 0 y num_colores-1.
    Sirve para iniciar el automata con un estado random.
 
    Entradas:
    - filas: numero de filas (int)
    - columnas: numero de columnas (int)
    - num_colores: cuantos colores diferentes hay (int)
 
    Salidas: matriz de filas x columnas con valores random
 
    Restricciones: todos los parametros deben ser enteros positivos
    """
    if type(filas) != int or filas <= 0:
        raise Exception("Las filas deben ser entero positivo")
 
    if type(columnas) != int or columnas <= 0:
        raise Exception("Las columnas deben ser entero positivo")
 
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(random.randint(0, num_colores - 1))
        matriz.append(fila)
    return matriz

def girar_hormiga(direccion, giro):
    """
    cambia la direccion de la hormiga segun el giro que se le da.
    La direccion esta guardada como un numero: 0=arriba, 1=derecha, 2=abajo, 3=izquierda.
    Girar a la derecha suma 1, girar a la izquierda resta 1 (con modulo 4 para que no se salga).
 
    Entradas:
    - direccion: direccion actual de la hormiga (int entre 0 y 3)
    - giro: 'R' para girar derecha, 'L' para girar izquierda (string)
 
    Salidas: la nueva direccion de la hormiga (int entre 0 y 3)
 
    Restricciones: giro solo puede ser 'R' o 'L', direccion entre 0 y 3
    """
    if giro == 'R':
        nueva = (direccion + 1) % 4  # sumar 1 gira a la derecha
    elif giro == 'L':
        nueva = (direccion - 1) % 4  # restar 1 gira a la izquierda
    else:
        raise Exception("El giro debe ser R o L")
 
    return nueva

def avanzar_hormiga(fila, col, direccion, filas_total, cols_total):
    """
    mueve la hormiga una celda hacia adelante segun su direccion actual.
    Si se sale de la matriz, aparece por el otro lado (tipo pac-man).
 
    Entradas:
    - fila: fila actual de la hormiga (int)
    - col: columna actual de la hormiga (int)
    - direccion: hacia donde va la hormiga (int: 0=arriba, 1=derecha, 2=abajo, 3=izquierda)
    - filas_total: cuantas filas tiene la matriz (int)
    - cols_total: cuantas columnas tiene la matriz (int)
 
    Salidas: tupla (nueva_fila, nueva_col) con la nueva posicion
 
    Restricciones: la direccion debe estar entre 0 y 3
    """
    if direccion == 0:    # arriba: la fila disminuye
        nueva_fila = (fila - 1) % filas_total
        nueva_col = col
    elif direccion == 1:  # derecha: la columna aumenta
        nueva_fila = fila
        nueva_col = (col + 1) % cols_total
    elif direccion == 2:  # abajo: la fila aumenta
        nueva_fila = (fila + 1) % filas_total
        nueva_col = col
    elif direccion == 3:  # izquierda: la columna disminuye
        nueva_fila = fila
        nueva_col = (col - 1) % cols_total
    else:
        raise Exception("Direccion invalida, debe ser 0, 1, 2 o 3")
 
    return nueva_fila, nueva_col

def siguiente(matriz, fila, col, direccion, reglas):
    """
    ejecuta un paso del automata. Mira en que color esta la hormiga,
    busca en las reglas que giro hacer, gira la hormiga, cambia el color de la celda
    y mueve la hormiga un paso.
 
    Entradas:
    - matriz: la cuadricula actual del automata (lista de listas de ints)
    - fila: fila donde esta la hormiga (int)
    - col: columna donde esta la hormiga (int)
    - direccion: hacia donde apunta la hormiga (int)
    - reglas: string de L y R, ejemplo 'LR' o 'LLRR' (string)
 
    Salidas: tupla (nueva_fila, nueva_col, nueva_direccion) con el estado actualizado
 
    Restricciones: las reglas deben contener solo L y R, la posicion debe ser valida
    """
    filas_total = len(matriz)
    cols_total = len(matriz[0])
    num_colores = len(reglas)
 
    # 1. vemos el color de la celda actual
    color_actual = matriz[fila][col]
 
    # 2. buscamos en las reglas que giro hacer para ese color
    giro = reglas[color_actual]
 
    # 3. giramos la hormiga
    nueva_direccion = girar_hormiga(direccion, giro)
 
    # 4. cambiamos el color de la celda al siguiente (ciclico)
    matriz[fila][col] = (color_actual + 1) % num_colores
 
    # 5. movemos la hormiga un paso
    nueva_fila, nueva_col = avanzar_hormiga(fila, col, nueva_direccion, filas_total, cols_total)
 
    return nueva_fila, nueva_col, nueva_direccion

def pedir_parametros():
    """
    Le pregunta al usuario los parametros del automata usando ventanas de easygui.
    Pide: filas, columnas, tamanio de celda y las reglas (string de L y R).
 
    Entradas: nada (le pregunta al usuario)
 
    Salidas: tupla con (filas, columnas, tam_celda, reglas) o None si el usuario cancela
 
    Restricciones: los valores numericos deben ser positivos, las reglas solo L y R
    """
    # pedimos las filas
    filas_str = easygui.enterbox(
        "Cuantas FILAS quieres para la cuadricula?\n(recomendado: entre 50 y 200)",
        title="Hormiga de Langton - Configuracion"
    )
    if filas_str is None:
        return None
 
    # pedimos las columnas
    cols_str = easygui.enterbox(
        "Cuantas COLUMNAS quieres?\n(recomendado: entre 50 y 200)",
        title="Hormiga de Langton - Configuracion"
    )
    if cols_str is None:
        return None
 
    # pedimos el tamanio de cada celda
    tam_str = easygui.enterbox(
        "Que tan grande quieres cada celda en pixeles?\n(recomendado: entre 4 y 10)",
        title="Hormiga de Langton - Configuracion"
    )
    if tam_str is None:
        return None
 
    # pedimos las reglas
    reglas_str = easygui.enterbox(
        "Escribe las reglas de la hormiga con L y R:\n"
        "Ejemplos:\n"
        "  LR  -> hormiga clasica\n"
        "  LLRR -> patrones simetricos\n"
        "  RLR  -> caos\n"
        "  LRRRRRLLR -> crece en cuadrado",
        title="Hormiga de Langton - Configuracion"
    )
    if reglas_str is None:
        return None
 
    # validamos que los numeros sean correctos
    try:
        filas = int(filas_str)
        columnas = int(cols_str)
        tam_celda = int(tam_str)
    except ValueError:
        easygui.msgbox("Los valores de filas, columnas y tamanio deben ser numeros enteros.", title="Error")
        return None
 
    if filas <= 0 or columnas <= 0 or tam_celda <= 0:
        easygui.msgbox("Los valores deben ser mayores a 0.", title="Error")
        return None
 
    # validamos que las reglas solo tengan L y R
    reglas_str = reglas_str.upper().strip()
    for letra in reglas_str:
        if letra != 'L' and letra != 'R':
            easygui.msgbox("Las reglas solo pueden tener L y R, por ejemplo: LR o LLRR", title="Error")
            return None
 
    if len(reglas_str) < 2:
        easygui.msgbox("Las reglas deben tener al menos 2 letras.", title="Error")
        return None
 
    return filas, columnas, tam_celda, reglas_str

def dibujar(pantalla, matriz, colores, tam_celda, fila_hormiga, col_hormiga):
    """
    dibuja la matriz en la ventana de pygame. Cada celda se pinta con
    el color que le corresponde segun su valor. La hormiga se marca con un punto rojo.
 
    Entradas:
    - pantalla: la ventana de pygame (pygame.Surface)
    - matriz: la cuadricula con los estados (lista de listas)
    - colores: lista de colores RGB (lista de tuplas)
    - tam_celda: tamanio de cada celda en pixeles (int)
    - fila_hormiga: fila donde esta la hormiga (int)
    - col_hormiga: columna donde esta la hormiga (int)
 
    Salidas: nada, dibuja directamente en la pantalla
 
    Restricciones: la pantalla debe estar inicializada, la hormiga debe estar dentro de la matriz
    """
    filas = len(matriz)
    cols = len(matriz[0])
 
    for f in range(filas):
        for c in range(cols):
            color = colores[matriz[f][c]]
            # calculamos la posicion en pixeles
            x = c * tam_celda
            y = f * tam_celda
            pygame.draw.rect(pantalla, color, (x, y, tam_celda, tam_celda))
 
    # dibujamos la hormiga encima de todo con un punto rojo
    x_h = col_hormiga * tam_celda
    y_h = fila_hormiga * tam_celda
    pygame.draw.rect(pantalla, (255, 0, 0), (x_h, y_h, tam_celda, tam_celda))

def guardar_estado(matriz, filas, columnas, tam_celda, reglas, fila_h, col_h, dir_h):
    """
    guarda todo el estado del automata en un archivo .pkl usando pickle.
    Guarda la matriz, dimensiones, tamanio, reglas y posicion de la hormiga.
 
    Entradas:
    - matriz: cuadricula actual (lista de listas)
    - filas: numero de filas (int)
    - columnas: numero de columnas (int)
    - tam_celda: tamanio de celda (int)
    - reglas: string de reglas LR (string)
    - fila_h: fila actual de la hormiga (int)
    - col_h: columna actual de la hormiga (int)
    - dir_h: direccion actual de la hormiga (int)
 
    Salidas: nada, crea el archivo guardado.pkl
 
    Restricciones: debe haber permisos de escritura en la carpeta
    """
    estado = {
        "matriz": matriz,
        "filas": filas,
        "columnas": columnas,
        "tam_celda": tam_celda,
        "reglas": reglas,
        "fila_hormiga": fila_h,
        "col_hormiga": col_h,
        "dir_hormiga": dir_h
    }
 
    with open("guardado_hormiga.pkl", "wb") as archivo:
        pickle.dump(estado, archivo)
 
    print("Estado guardado en guardado_hormiga.pkl")

def cargar_estado():
    """
    carga el estado del automata desde un archivo .pkl guardado antes.
    Si el archivo no existe, avisa y retorna None.
 
    Entradas: nada
 
    Salidas: diccionario con todo el estado guardado, o None si no existe el archivo
 
    Restricciones: debe existir el archivo guardado_hormiga.pkl
    """
    try:
        with open("guardado_hormiga.pkl", "rb") as archivo:
            estado = pickle.load(archivo)
        print("Estado cargado desde guardado_hormiga.pkl")
        return estado
    except FileNotFoundError:
        print("No se encontro el archivo guardado_hormiga.pkl")
        easygui.msgbox("No hay ningun archivo guardado todavia!", title="Error al cargar")
        return None

def correr_hormiga():
    """
    funcion principal que corre todo el loop del automata de la hormiga de Langton.
    Primero pide los parametros, luego corre pygame con el loop principal.
    Maneja todos los eventos del teclado y mouse.
 
    Entradas: nada (le pide al usuario lo que necesita)
 
    Salidas: nada
 
    Restricciones: requiere pygame y easygui instalados
    """
    global hormiga_fila, hormiga_col, hormiga_direccion
 
    # pedimos parametros al usuario
    params = pedir_parametros()
    if params is None:
        return  # el usuario cancelo
 
    filas, columnas, tam_celda, reglas = params
    num_colores = len(reglas)
 
    # creamos la matriz vacia y la hormiga en el centro
    matriz = generar_matriz_vacia(filas, columnas)
    hormiga_fila = filas // 2
    hormiga_col = columnas // 2
    hormiga_direccion = 0
 
    # generamos los colores segun cuantos necesitamos
    colores = generar_colores(num_colores)
 
    # iniciamos pygame
    pygame.init()
    ancho = columnas * tam_celda
    alto = filas * tam_celda
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(f"Hormiga de Langton - Reglas: {reglas}")
    reloj = pygame.time.Clock()
 
    corriendo = True
    pausado = False
 
    while corriendo:
        # procesamos eventos
        for evento in pygame.event.get():
 
            if evento.type == pygame.QUIT:
                corriendo = False
 
            elif evento.type == pygame.KEYDOWN:
 
                if evento.key == pygame.K_SPACE:
                    # espacio pausa y despausa
                    pausado = not pausado
                    if pausado:
                        print("Pausado")
                    else:
                        print("Corriendo")
 
                elif evento.key == pygame.K_r:
                    # R reinicia con matriz aleatoria
                    matriz = generar_matriz_aleatoria(filas, columnas, num_colores)
                    hormiga_fila = filas // 2
                    hormiga_col = columnas // 2
                    hormiga_direccion = 0
                    print("Matriz reiniciada aleatoriamente")
 
                elif evento.key == pygame.K_b:
                    # B limpia todo (matriz en ceros)
                    matriz = generar_matriz_vacia(filas, columnas)
                    hormiga_fila = filas // 2
                    hormiga_col = columnas // 2
                    hormiga_direccion = 0
                    print("Matriz reiniciada a ceros")
 
                elif evento.key == pygame.K_g:
                    # G guarda el estado
                    guardar_estado(matriz, filas, columnas, tam_celda, reglas,
                                   hormiga_fila, hormiga_col, hormiga_direccion)
 
                elif evento.key == pygame.K_c:
                    # C carga un estado guardado
                    estado = cargar_estado()
                    if estado is not None:
                        matriz = estado["matriz"]
                        filas = estado["filas"]
                        columnas = estado["columnas"]
                        tam_celda = estado["tam_celda"]
                        reglas = estado["reglas"]
                        hormiga_fila = estado["fila_hormiga"]
                        hormiga_col = estado["col_hormiga"]
                        hormiga_direccion = estado["dir_hormiga"]
                        num_colores = len(reglas)
                        colores = generar_colores(num_colores)
 
                        # redimensionamos la ventana si cambio el tamanio
                        ancho = columnas * tam_celda
                        alto = filas * tam_celda
                        pantalla = pygame.display.set_mode((ancho, alto))
                        pygame.display.set_caption(f"Hormiga de Langton - Reglas: {reglas}")
 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # click del mouse cambia el color de la celda al siguiente
                mx, my = pygame.mouse.get_pos()
                col_click = mx // tam_celda
                fila_click = my // tam_celda
 
                if 0 <= fila_click < filas and 0 <= col_click < columnas:
                    # avanzamos el color al siguiente (ciclico)
                    color_actual = matriz[fila_click][col_click]
                    matriz[fila_click][col_click] = (color_actual + 1) % num_colores
 
        # si no esta pausado, hacemos un paso del automata
        if not pausado:
            hormiga_fila, hormiga_col, hormiga_direccion = siguiente(
                matriz, hormiga_fila, hormiga_col, hormiga_direccion, reglas
            )
 
        # dibujamos todo
        pantalla.fill((200, 200, 200))  # fondo gris por si acaso
        dibujar(pantalla, matriz, colores, tam_celda, hormiga_fila, hormiga_col)
        pygame.display.flip()
        reloj.tick(60)  # maximo 60 fps
 
    pygame.quit()

# =====================================================================
# MENU PRINCIPAL - INTERFAZ LISTAAAAAAAAAAAAAA
# =====================================================================
def main():
    """
    muestra un menu para que el usuario elija que automata quiere usar.
    Entradas: nada
    Salidas: nada, llama a la funcion del automata elegido
    Antonio Ye Lu 
    -David Rodríguez Zúñiga
    """
    opciones = [
        "Juego de la vida(Life-Like)"
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
            
        elif eleccion == "Juego de la vida(Life-Like)":
            likeLife()


if __name__ == "__main__":
    main()
