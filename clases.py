import random
import numpy as np
import constantes

class Tableros():
    """Clase creada para generar los 3 tableros (usuario, maquina, maquina_copia)"""
    matriz = np.full((10,10), fill_value = "_")
    def __init__(self, nombre):
        self.nombre = nombre
    
    # def tableros(self):
    #     tablero_user = np.full((10,10), fill_value = "_")
        # tablero_computer = np.full((10,10), fill_value = "_")
        # tablero_copy = np.full((10,10), fill_value = "_")
        # return tablero_user, tablero_computer, tablero_copy
    
    def poner_barcos(self):
        lista_barcos = constantes.barcos
        
        # para acceder a las coordenadas --> tablero_user.matriz[2,4]
        for i in lista_barcos:
      
            ok = False
        
        while ok == False:
                fila_barco = random.randint(0,9)
                columna_barco = random.randint(0,9)
                direccion = random.choice(["N", "S", "E", "O"])
                eslora = i

                if direccion == "N" and fila_barco + eslora -1 < len(self.matriz):
                    ok = True
                    for x in range(fila_barco,fila_barco + eslora):
                            if self.matriz[x, columna_barco] == "O":
                                ok = False
                    if ok == True:
                            self.matriz[fila_barco:fila_barco + eslora, columna_barco] = "O"
                            #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion) #estos prints he creado simplemente para ayudarme con la logica de poner los barcos de forma aleatoria. Así que en el momento de jugar los mismos no deberán imprimir.
                elif direccion == "S" and fila_barco - eslora +1 >= 0:
                    ok = True
                    for x in range(fila_barco - eslora +1,fila_barco +1):
                            if self.matriz[x, columna_barco] == "O":
                                ok = False
                    if ok == True:
                            self.matriz[fila_barco - eslora +1: fila_barco +1, columna_barco] = "O"
                            #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion) #estos prints he creado simplemente para ayudarme con la logica de poner los barcos de forma aleatoria. Así que en el momento de jugar los mismos no deberán imprimir.
                elif direccion == "E" and columna_barco + eslora -1 < len(self.matriz):
                    ok = True
                    for x in range(columna_barco,columna_barco + eslora):
                            if self.matriz[fila_barco, x] == "O":
                                ok = False
                    if ok == True:
                            self.matriz[fila_barco, columna_barco: columna_barco + eslora] = "O"
                            #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion) #estos prints he creado simplemente para ayudarme con la logica de poner los barcos de forma aleatoria. Así que en el momento de jugar los mismos no deberán imprimir.
                elif direccion == "O" and columna_barco - eslora +1 >= 0:
                    ok = True
                    for x in range(columna_barco - eslora +1,columna_barco +1):
                            if self.matriz[fila_barco, x] == "O":
                                ok = False
                    if ok == True:
                            self.matriz[fila_barco, columna_barco - eslora +1: columna_barco +1] = "O"
                            #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion)
                                    #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion)
        
        # for i in lista_barcos:
            
        #     ok = False
            
        #     while ok == False:
        #             fila_barco = random.randint(0,9)
        #             columna_barco = random.randint(0,9)
        #             direccion = random.choice(["N", "S", "E", "O"])
        #             eslora = i

        #             if direccion == "N" and fila_barco + eslora -1 < len(tablero_computer):
        #                 ok = True
        #                 for x in range(fila_barco,fila_barco + eslora):
        #                         if tablero_computer[x, columna_barco] == "O":
        #                             ok = False
        #                 if ok == True:
        #                         tablero_computer[fila_barco:fila_barco + eslora, columna_barco] = "O"
        #                         #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion)
        #             elif direccion == "S" and fila_barco - eslora +1 >= 0:
        #                 ok = True
        #                 for x in range(fila_barco - eslora +1,fila_barco +1):
        #                         if tablero_computer[x, columna_barco] == "O":
        #                             ok = False
        #                 if ok == True:
        #                         tablero_computer[fila_barco - eslora +1: fila_barco +1, columna_barco] = "O"
        #                         #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion)
        #             elif direccion == "E" and columna_barco + eslora -1 < len(tablero_computer):
        #                 ok = True
        #                 for x in range(columna_barco,columna_barco + eslora):
        #                         if tablero_computer[fila_barco, x] == "O":
        #                             ok = False
        #                 if ok == True:
        #                         tablero_computer[fila_barco, columna_barco: columna_barco + eslora] = "O"
        #                         #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion)
        #             elif direccion == "O" and columna_barco - eslora +1 >= 0:
        #                 ok = True
        #                 for x in range(columna_barco - eslora +1,columna_barco +1):
        #                         if tablero_computer[fila_barco, x] == "O":
        #                             ok = False
        #                 if ok == True:
        #                         tablero_computer[fila_barco, columna_barco - eslora +1: columna_barco +1] = "O"
        #                         #print("navio: ", i, " - fila: ", fila_barco, " - columna: ", columna_barco, " - Dir: ", direccion)


class Juego():
    
    def __init__(self):
        print("----Bienvenido al juego Hundir de la Flota!----")
        print("-----El partido será entre tu y la máquina-----")
        print("--------------------Suerte!--------------------")
        print()
        print("**Las instrucciones del partido son las siguientes:**")
        print(" 1 - Tanto tu, como la máquina tenéis un tablero con barcos, y se trata de ir disparando y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.", "\n", "2 - Funciona por turnos y empiezas tú.", "\n", "3 - En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.", "\n","4- En los turnos de la máquina, si acerta también le vuelve a tocar.", "\n", "5 - Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.")


    

    def disparos(tablero):
        

        while "O" in tablero and "O" in tablero:

            #juega el user

            while "O" in tablero and "O" in tablero:

                print("Juegas tu!")

                user_disparo_1 = int(input("1 - Indicar fila entre 0 y 9: "))
                user_disparo_2 = int(input("2 - Indicar columna entre 0 y 9: "))

                if user_disparo_1 > 9 or user_disparo_1 < 0 or user_disparo_2 > 9 or user_disparo_2 < 0:

                    print("Has incluido una coordenada fuera del tablero") 

                elif tablero[user_disparo_1, user_disparo_2] == "_":
                    tablero[user_disparo_1, user_disparo_2] = "A"
                    tablero[user_disparo_1, user_disparo_2] = "A"
                    print("Agua!!!")
                    print("Tablero_maquina:","\n",tablero)
                    print("\n")
                    break
                    
                elif tablero[user_disparo_1, user_disparo_2] == "O":
                    tablero[user_disparo_1, user_disparo_2] = "X"
                    tablero[user_disparo_1, user_disparo_2] = "X"
                    exists =  "O" in tablero
                    if exists == False:
                        print("Enhorabuena, has destrozado la maquina!!!")
                        break
                    print("Has identificado un barco, puedes jugar otra vez!!!")
                    print("Tablero_maquina:","\n",tablero)
                    print("\n")
                                
                elif tablero[user_disparo_1, user_disparo_2] == "X":
                    
                    print("Coordenada ya disparada, inténtalo de nuevo!!!")
                    print("\n")

                elif tablero[user_disparo_1, user_disparo_2] == "A":
                    
                    print("Coordenada ya disparada, inténtalo de nuevo!!!")
                    print("\n")


            #juega la maquina

            while "O" in tablero and "O" in tablero:

                print("Juega la maquina!")

                maquina_disparo_1 = random.randint(0,9)
                maquina_disparo_2 = random.randint(0,9)

                if tablero_user[maquina_disparo_1, maquina_disparo_2] == "_":
                    tablero_user[maquina_disparo_1, maquina_disparo_2] = "A"
                    print("Agua!!!")
                    print("Tablero_user:","\n",tablero_user)
                    print("\n")
                    print("Tablero_maquina:","\n",tablero_copy)
                    print("\n")
                    break

                elif tablero_user[maquina_disparo_1, maquina_disparo_2] == "O":
                    tablero_user[maquina_disparo_1, maquina_disparo_2] = "X"
                    exists2 =  "O" in tablero_user
                    if exists2 == False:
                        print("Enhorabuena, has destrozado tu oponente humano!!!")
                        break 
                    print("La maquina ha identificado un barco y puede jugar otra vez!!!", "\n", tablero_user)
                    print("\n")
                                
                elif tablero_user[maquina_disparo_1, maquina_disparo_2] == "X":
                    print("Coordinada ya disparada, la maquina puede intentar otra vez!!!")
                    print("\n")

                elif tablero_user[maquina_disparo_1, maquina_disparo_2] == "A":
                    print("Coordinada ya disparada, la maquina puede intentar otra vez!!!")
                    print("\n")

        else:
            print("-----Fin de juego-----")
            print("By Hugo Meschini (with a 'little' help from The Bridge teachers and friends)")
                
