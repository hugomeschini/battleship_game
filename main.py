#importar
from clases import *

tablero_computer = Tableros('tablero computer')
tablero_user = Tableros('tablero user')
tablero_copy = Tableros('tablero copy')

tablero_computer.poner_barcos()
tablero_user.poner_barcos()

juego = Juego

juego.disparos(tablero_computer.matriz)

