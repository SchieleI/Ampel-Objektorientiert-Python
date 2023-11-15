class Ampel(object):
    def __init__(self):
        self.__zustand = 'rot'

    def schalten(self):
        if self.__zustand == 'rot':
            self.__zustand = 'rotgelb'
        elif self.__zustand == 'rotgelb':
            self.__zustand = 'gruen'
        elif self.__zustand == 'gruen':
            self.__zustand = 'gelb'
        elif self.__zustand == 'gelb':
            self.__zustand = 'rot'

    def getLampen(self):
        if self.__zustand == 'rot':
            lampen = (True, False, False)
        elif self.__zustand == 'rotgelb':
            lampen = (True, True, False)
        elif self.__zustand == 'gruen':
            lampen = (False, False, True)
        elif self.__zustand == 'gelb':
            lampen = (False, True, False)
        return lampen

    def getZustand(self):
        return self.__zustand

    def setZustand(self, z):
        self.__zustand = z