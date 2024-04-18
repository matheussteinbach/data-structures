from elemento import Elemento


class ListaDuplamenteEncadeada:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__inicio = None
        self.__fim = None
        self.__cursor = self.__inicio

    def acessar_atual(self) -> Elemento:
        return self.__cursor

    def inserir_antes_do_atual(self, novo):
        novo_elemento = Elemento(novo)
        if not self.__inicio:
            self.__inicio = novo_elemento
            self.__fim = novo_elemento
        else:
            novo_elemento.proximo = self.__cursor
            self.__cursor.anterior.proximo = novo_elemento
            novo_elemento.anterior = self.__cursor.anterior
            self.__cursor.anterior = novo_elemento

    def inserir_apos_atual(self, novo):
        novo_elemento = Elemento(novo)
        if not self.__inicio:
            self.__inicio = novo_elemento
            self.__fim = novo_elemento
        else:
            novo_elemento.anterior = self.__cursor
            self.__cursor.proximo.anterior = novo_elemento
            novo_elemento.proximo = self.__cursor.proximo
            self.__cursor.proximo = novo_elemento

    def inserir_como_ultimo(self, novo):
        novo_elemento = Elemento(novo)
        if not self.__fim:
            self.__inicio = novo_elemento
        else:
            novo_elemento.anterior = self.__fim
            self.__fim.proximo = novo_elemento
        self.__fim = novo_elemento

    def inserir_como_primeiro(self, novo):
        novo_elemento = Elemento(novo)
        if not self.__inicio:
            self.__fim = novo_elemento
        else:
            novo_elemento.proximo = self.__inicio
            self.__inicio.anterior = novo_elemento
        self.__inicio = novo_elemento

    def inserir_na_posicao(self, k, novo):
        novo_elemento = Elemento(novo)

    def excluir_atual(self):
        if not self.__inicio:
            return
        self.__cursor.anterior.proximo = self.__cursor.proximo
        self.__cursor.proximo.anterior = self.__cursor

    def excluir_prim(self):
        if not self.__inicio:
            return
        self.__inicio.proximo.anterior = None
        self.__inicio = self.__inicio.proximo

    def excluir_ult(self):
        if not self.__fim:
            return
        self.__fim.anterior.proximo = None
        self.__fim = self.__fim.anterior

    def excluir_elem(self, chave):
        pass

    def excluir_da_pos(self, k):
        pass

    def buscar(self, chave) -> Elemento:
        pass

    def avancar_k_posicoes(self, k):
        for i in range(k):
            self.__cursor = self.__cursor.proximo

    def retroceder_k_posicoes(self, k):
        for i in range(k):
            self.__cursor = self.__cursor.anterior

    def ir_para_primeiro(self):
        self.__cursor = self.__inicio

    def ir_para_ultimo(self):
        self.__cursor = self.__fim
