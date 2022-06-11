import mazo
import collections

def anillo():
    cartas = mazo.Mazo()
    carta = []
    match = [False for x in range(1,14)]
    posicion = [[] for x in range(1,14)]
    i = 0
    while len(cartas.mazo):
        try:
            for i in range(len(posicion)):
                if match[i] == False:
                    #print("Cantidad de cartas restantes:", len(cartas.mazo))
                    carta = cartas.sacar_carta()
                    posicion[i%len(posicion)].append(carta)
                    if carta[1] == i+1:
                        match[i] = True
                        for a in range(len(posicion[i])-1):
                            cartas.colocar_carta(posicion[i][a])
                        posicion[i%len(posicion)] = carta
            if(all(match)):
                print("Has ganado!")
                return True                             
        except:
            print("No hay mas cartas! Juego terminado.")
            return False 

if __name__ == '__main__':
    anillo()