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
            if not self.__inicio or not self.__cursor.proximo:
                self.inserir_como_primeiro(novo)
            else:
                novo_elemento.proximo = self.__cursor
                self.__cursor.anterior.proximo = novo_elemento
                novo_elemento.anterior = self.__cursor.anterior
                self.__cursor.anterior = novo_elemento
                self.__contador += 1

    def inserir_apos_atual(self, novo):
        if not self.cheia():
            novo_elemento = Elemento(novo)
            if not self.__inicio or not self.__cursor.anterior:
                self.inserir_como_ultimo(novo)
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
            self.buscar_por_posicao(k)
            self.inserir_antes_do_atual(novo)
            self.__retroceder_k_posicoes(1)

    def excluir_atual(self):
        if not self.vazia():
            if self.__cursor == self.__inicio:
                self.excluir_prim()
            elif self.__cursor == self.__fim:
                self.excluir_ult()
            else:
                self.__cursor.anterior.proximo = self.__cursor.proximo
                self.__retroceder_k_posicoes(1)
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
            self.buscar_por_chave(chave)
            self.excluir_atual()

    def excluir_da_pos(self, k):
        if not self.vazia():
            self.buscar_por_posicao(k)
            self.excluir_atual()

    def buscar_por_chave(self, chave) -> bool:
        self.__ir_para_primeiro()
        for i in range(self.__contador):
            if chave == self.__cursor.identificador:
                return True
            self.__avancar_k_posicoes(1)
        return False

    def buscar_por_posicao(self, k) -> bool:
        if self.__contador < k:
            return False
        else:
            self.__ir_para_primeiro()
            self.__avancar_k_posicoes(k - 1)
            return True

    def __avancar_k_posicoes(self, k):
        try:
            for i in range(k):
                self.__cursor = self.__cursor.proximo
        except AttributeError:
            return

    def __retroceder_k_posicoes(self, k):
        try:
            for i in range(k):
                self.__cursor = self.__cursor.anterior
        except AttributeError:
            return

    def __ir_para_primeiro(self):
        self.__cursor = self.__inicio

    def __ir_para_ultimo(self):
        self.__cursor = self.__fim

    def vazia(self) -> bool:
        return not self.__contador

    def cheia(self) -> bool:
        return self.__contador == self.__tamanho
