'''
Faça você mesmo!
Em duplas, escrever um algoritmo para descobrir a altura da
pessoa mais alta de um grupo de pessoas. Suponha que estas
pessoas estão em seqüência, como em uma fila de banco, e que
esta fila não está vazia.

'''

qtdPessoas = int(input('Informe quantas pessoas você vai adicionar:\n'))
alturaPessoas = list(range(qtdPessoas))

alturaMaxima = 0;

i = 0
while i<qtdPessoas:
    alturaPessoas[i] = float(input('Informe a altura da  pessoa:\n'))
    if alturaPessoas[i] > alturaMaxima:
        alturaMaxima = alturaPessoas[i]
    i += 1
print('A pessoa mais alta é {:.2f} de altura'.format(alturaMaxima))
