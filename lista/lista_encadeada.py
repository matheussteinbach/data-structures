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
        ponteiro = self.__inicio
        while ponteiro.proximo:
            atual = ponteiro.proximo
            if pos == contador:
                ponteiro.proximo = atual.proximo
                if atual.proximo == None:
                    self.__fim = ponteiro
                return atual
            contador += 1
            ponteiro = atual
    
    def acesso_primeiro(self):
        return self.__inicio

    def acesso_ultimo(self):
        return self.__fim

    def busca_por_id(self, id):
        if self.__inicio.identificador == id:
            return self.__inicio
        ponteiro = self.__inicio
        while ponteiro.proximo:
            atual = ponteiro.proximo
            if atual.identificador == id:
                return atual
            ponteiro = atual

    def excluir_por_id(self, id):
        if self.__inicio.identificador == id:
            self.remover_primeiro()
        ponteiro = self.__inicio
        while ponteiro.proximo:
            atual = ponteiro.proximo
            if atual.identificador == id:
                ponteiro.proximo = atual.proximo
                if atual.proximo == None:
                    self.__fim = ponteiro
                return atual
            ponteiro = atual
