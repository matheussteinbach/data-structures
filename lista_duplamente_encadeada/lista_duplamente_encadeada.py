from elemento import Elemento


class ListaDuplamenteEncadeada:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__inicio = None
        self.__fim = None
        self.__cursor = self.__inicio
        self.__contador = 0

    def acessar_atual(self) -> Elemento:
        return self.__cursor

    def inserir_antes_do_atual(self, novo):
        if not self.cheia():
            novo_elemento = Elemento(novo)
            if not self.__inicio:
                self.__inicio = novo_elemento
                self.__fim = novo_elemento
            else:
                novo_elemento.proximo = self.__cursor
                self.__cursor.anterior.proximo = novo_elemento
                novo_elemento.anterior = self.__cursor.anterior
                self.__cursor.anterior = novo_elemento
                self.__contador += 1

    def inserir_apos_atual(self, novo):
        if not self.cheia():
            novo_elemento = Elemento(novo)
            if not self.__inicio:
                self.__inicio = novo_elemento
                self.__fim = novo_elemento
            else:
                novo_elemento.anterior = self.__cursor
                self.__cursor.proximo.anterior = novo_elemento
                novo_elemento.proximo = self.__cursor.proximo
                self.__cursor.proximo = novo_elemento
                self.__contador += 1

    def inserir_como_ultimo(self, novo):
        if not self.cheia():
            novo_elemento = Elemento(novo)
            if not self.__fim:
                self.__inicio = novo_elemento
            else:
                novo_elemento.anterior = self.__fim
                self.__fim.proximo = novo_elemento
            self.__fim = novo_elemento
            self.__contador += 1

    def inserir_como_primeiro(self, novo):
        if not self.cheia():
            novo_elemento = Elemento(novo)
            if not self.__inicio:
                self.__fim = novo_elemento
            else:
                novo_elemento.proximo = self.__inicio
                self.__inicio.anterior = novo_elemento
            self.__inicio = novo_elemento
            self.__contador += 1

    def inserir_na_posicao(self, k, novo):
        if not self.cheia():
            self.buscar(k)
            self.inserir_antes_do_atual(Elemento(novo))
            self.retroceder_k_posicoes(1)v

    def excluir_atual(self):
        if not self.vazia():
            self.__cursor.anterior.proximo = self.__cursor.proximo
            self.__cursor.proximo.anterior = self.__cursor
            self.__contador -= 1

    def excluir_prim(self):
        if not self.vazia():
            self.__inicio.proximo.anterior = None
            self.__inicio = self.__inicio.proximo
            self.__contador -= 1

    def excluir_ult(self):
        if not self.vazia():
            self.__fim.anterior.proximo = None
            self.__fim = self.__fim.anterior
            self.__contador -= 1

    def excluir_elem(self, chave):
        if not self.vazia():
            self.buscar(chave)
            self.excluir_atual()

    def excluir_da_pos(self, k):
        if not self.vazia():
            self.buscar(k)
            self.excluir_atual()

    def buscar(self, chave) -> bool:
        self.ir_para_primeiro()
        posicao = 1
        for i in range(self.__contador):
            if chave == self.__cursor.identificador or \
                    chave == posicao:
                return True
            self.avancar_k_posicoes(1)
            posicao += 1
        return False

    def avancar_k_posicoes(self, k):
        try:
            for i in range(k):
                self.__cursor = self.__cursor.proximo
        except AttributeError:
            self.__cursor = self.__fim

    def retroceder_k_posicoes(self, k):
        try:
            for i in range(k):
                self.__cursor = self.__cursor.anterior
        except AttributeError:
            self.__cursor = self.__inicio

    def ir_para_primeiro(self):
        self.__cursor = self.__inicio

    def ir_para_ultimo(self):
        self.__cursor = self.__fim

    def vazia(self) -> bool:
        if not self.__contador:
            return True
        return False

    def cheia(self) -> bool:
        if self.__contador == self.__tamanho:
            return True
        return False
