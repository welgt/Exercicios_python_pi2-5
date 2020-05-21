#1, 2, 3, 5, 8, 13, 21, 34, 55,...

def fibonaci(n):
    anterior = 1
    atual = 1
    print(anterior)
    print(atual)
    i = 0
    while i < n:
        atual = atual + anterior
        print(atual)
        anterior = atual - anterior
        i = i + 1

n = int(input('Informe o tamanho da sequencia de Fibonaci:\n'))
fibonaci(n)



























































