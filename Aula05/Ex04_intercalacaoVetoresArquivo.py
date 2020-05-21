def intercalacao(a,b):


    c = ['*'] * (len(a) + len(b))

    i = 0
    for A in a:
        c[i] = A
        i+=1

    j = len(a)
    for B in b:
        c[j] = B
        j+=1

    c.sort()
    print(c)



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

        intercalacao(v1, v2)

    except:
        print("Erro ao tentar manipular o arquivo")

leitura("arquivos/Ex04.txt")