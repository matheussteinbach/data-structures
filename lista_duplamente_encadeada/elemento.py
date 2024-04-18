

class Elemento:
    def __init__(self, identificador):
        self.__identificador = identificador
        self.__anterior = None
        self.__proximo = None

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo
