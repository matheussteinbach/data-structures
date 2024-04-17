

class Array:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__array = [None] * tamanho

    @property
    def array(self):
        return self.__array

    def atribuir(self, pos, valor):
        self.acessa(pos) == valor

    def acessa(self, pos):
        return self.array[pos]
