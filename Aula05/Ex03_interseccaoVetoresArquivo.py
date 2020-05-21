
def interseccao(a,b):
    c = ['*'] * (len(a) + len(b))

    i = 0
    for A in a:
        for B in b:
            if A == B:
                c[i] = B
        if c[i] != '*':
            print(c[i], end=" ")
        i += 1

def leitura(arquivo1):

    try:
        arquivoLeitura = open(arquivo1, 'r')
        texto = arquivoLeitura.readlines()

        a = list(list(texto[0]))
        b = list(list(texto[1]))

        v1 = []
        v2 = []

        for c in a:
            if c == '\n' and c != "":
                a.remove(c)
            if c != '\n':
                v1.append(int(c))

        for c in b:
            if c == '\n' and c != "":
                b.remove(c)
            if c != '\n':
                v2.append(int(c))
        print("Vetor a:", v1)
        print("Vetor b:", v2)

        arquivoLeitura.close()
        interseccao(v1, v2)

    except:
        print("Erro ao tentar manipular o arquivo")



leitura("arquivos/Ex03.txt")