from lista_encadeada import ListaEncadeada


lista = ListaEncadeada()
lista.insira_primeiro("Davi")
lista.insira_primeiro("Theus")
lista.insira_ultimo("Ale")

teste = lista.remover_posicao(1)
print(teste.identificador)
print(lista.acesso_primeiro().identificador)
print(lista.acesso_ultimo().identificador)
