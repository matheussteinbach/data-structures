from lista.lista_encadeada import ListaEncadeada


class Hash:
    def __init__(self, tamanho, carga):
        self.__tamanho = tamanho
        self.__carga = carga
        self.__grupos = self.__tamanho // self.__carga
        self.__array = [ListaEncadeada()] * self.__grupos

    def incluir(self, id):
        posicao = id % self.__grupos
        self.__array[posicao].insira_ultimo(id)
        
    def buscar(self, id):
        posicao = id % self.__grupos
        return self.__array[posicao].busca_por_id(id)

    def excluir(self, id):
        posicao = id % self.__grupos
        self.__array[posicao].excluir_por_id(id)
