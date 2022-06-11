import random

class Mazo:
    __mazo__ = {
            "pics": [1,2,3,4,5,6,7,8,9,10,11,12,13],
            "trebol": [1,2,3,4,5,6,7,8,9,10,11,12,13],
            "corazon": [1,2,3,4,5,6,7,8,9,10,11,12,13],
            "diamante": [1,2,3,4,5,6,7,8,9,10,11,12,13]
            }
    mazo = []
    def __init__(self):
        for i in self.__mazo__.keys():
            for j in self.__mazo__[i]:
                self.mazo.append([i, j])
        self.mezclar()

    def __repr__(self):
        return str(self.mazo)

    def mezclar(self):
        return random.shuffle(self.mazo)

    def sacar_carta(self):
        return self.mazo.pop(0)
    
    def colocar_carta(self, carta):
        return self.mazo.append(carta)
        
    def reiniciar(self):
        self.__init__()