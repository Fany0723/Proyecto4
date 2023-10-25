import os #libreria os
from readchar import readkey, key #libreria Leer Caracter

################################################################
#   FUNCION LIMPIAR PANTALLA
################################################################
def mostrarMapa(mapa: list[list[str]]):
    os.system('cls') #limpiar pantalla
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            print(mapa[i][j], end="")
        print('')

################################################################
#   FUNCION PRINCIPAL MAINLOOP
################################################################
def mainLoop(mapa: list[list[str]], posini: tuple[int, int], posfin: tuple[int, int]):
    px,py = posini
    mapa[px][py]= 'P'
    mover = True
    mensaje = ''
    while (px,py) != posfin:
        #Mostrar Mapa y Mensajes
        mostrarMapa(mapa) #Mostrar Mapa        
        print(mensaje) #mostrar Mensaje
        print('Posicion del Jugador: ',(px , py) )
        
        #Movimiento del Tecleado
        print( 'movimientos ← ↑ ↓ → ')
        k = readkey()        
        if k == key.UP:
            px -= 1
        elif k == key.DOWN:
            px += 1
        elif k == key.LEFT:
            py -= 1
        elif k == key.RIGHT:
            py += 1
        else:
            mensaje = 'Tecla Invalida!!'

        #limite del Laberinto
        if (px, py) < posini or (py, py) > posfin:
            mensaje = 'la Unica Forma de salir del laberinto es llegando al Final!!'
        
        if mover:
            posactual = posini
            for row in range(len(mapa)):
                for col in range(len(mapa[i])):
                    if mapa[row][col] == 'P':
                        posactual = (row, col)
                        break

            if mapa[px][py] == '.': 
                mapa[posactual[0]][posactual[1]] = '.'                      
                mapa[px][py] = 'P'
                mover = True
                mensaje = 'Movimiento Valido!!'
            elif mapa[px][py] == '#': 
                px, py = posactual
                mensaje = 'Hay una Pared'
    mostrarMapa(mapa) #Mostrar Mapa 
    print("¡Has llegado a la posición final!")            
        

################################################################
#   INICIO DE APLICACION
################################################################
str_mapa = "..###################\n..#.....#...........#\n#.#####.#####.#.#.#.#\n#.#...#.#.#...#.#.#.#\n#.#.###.#.#.#.#####.#\n#.......#...#...#...#\n#.#####.###.#####.###\n#...#.....#.#...#...#\n#.#####.#####.###.###\n#...#.#...#.......#.#\n#.###.#.###.#.#####.#\n#...#.#.#.#.#.#...#.#\n###.#.###.###.###.#.#\n#.#.#...#.....#.....#\n#.#.###.#.#######.#.#\n#...............#.#.#\n#.#.#########.###.###\n#.#...#.....#...#.#.#\n#.#####.###.###.#.#.#\n#.....#...#.........#\n###################.."
mapa_array = str_mapa.split("\n")
mapa = list()
for i in range( len(mapa_array)):
    mapa.append( list(mapa_array[i]) )

posini = (0,0)
posfin = ( len(mapa) - 1, len(mapa[0])-1 )
mainLoop(mapa, posini, posfin)