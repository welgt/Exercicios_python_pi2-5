def contarCaracterArquivo(arquivo1):

    try:
        arquivoLeitura = open(arquivo1, 'r')
        texto = arquivoLeitura.readlines()

        novoTexto = []

        for linha in texto:
            for c in linha:
                novoTexto.append(c)

        novaPalavra = []

        for letra in novoTexto:
            if letra not in novaPalavra:
                novaPalavra.append(letra)
        for letra in novaPalavra:
            if letra != "\n" and letra != " ":
                print("contagen da letra: ", letra, ": ", novoTexto.count(letra))

        arquivoLeitura.close()

    except:
        print("Erro ao tentar manipular o arquivo")

contarCaracterArquivo("arquivos/Ex02.txt")