from elemento import Elemento


class ListaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def insira_primeiro(self, novo):
        novo_em = Elemento(novo)
        novo_em.proximo = self.__inicio
        if self.__inicio == None:
            self.__fim = novo_em
        self.__inicio = novo_em

    def insira_ultimo(self, novo):
        novo_em = Elemento(novo)
        if self.__fim == None:
            self.__inicio = novo_em
        else:
            self.__fim.proximo = novo_em
        self.__fim = novo_em

    def remover_primeiro(self):
        if self.__inicio == None:
            return
        self.__inicio = self.__inicio.proximo
        if self.__inicio == None:
            self.__fim = None

    def remover_posicao(self, pos):
        if pos == 0:
            self.remover_primeiro()
        contador = 1
        iterador = self.__inicio
        while iterador.proximo:
            atual = iterador.proximo
            if pos == contador:
                iterador.proximo = atual.proximo
                if atual.proximo == None:
                    self.__fim = iterador
                return atual
            contador += 1
            iterador = atual
    
    def acesso_primeiro(self):
        return self.__inicio

    def acesso_ultimo(self):
        return self.__fim

    def busca_por_id(self, id):
        if self.__inicio.identificador == id:
            return self.__inicio
        atual = self.__inicio
        while atual.proximo:
            if atual.proximo.identificador == id:
                return atual.proximo, atual
            atual = atual.proximo

    def excluir_por_id(self, id):
        ponteiro, anterior = self.busca_por_id(id)
        if ponteiro == self.__inicio:
            self.remover_primeiro()
        else:
            anterior.proximo = ponteiro.proximo
        
