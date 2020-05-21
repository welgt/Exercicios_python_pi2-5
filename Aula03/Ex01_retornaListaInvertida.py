
def listaInvertida(lista,tamanho):
    i = 0
    j = tamanho
    aux = list(range(tamanho))

    while i < tamanho:
        lista[i] = input('Informe os elementos da lista:\n')
        aux[j - 1] = lista[i]
        i += 1
        j -= 1

    print(aux)

tamanho = int(input('Informe o tamanho da lista:\n'))
lista = list(range(tamanho))

listaInvertida(lista,tamanho)







