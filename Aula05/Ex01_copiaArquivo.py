def copiarArquivo(arquivo1, arquivo2):
    try:
        arquivoLeitura = open(arquivo1, 'r')
        arquivoCopia = open(arquivo2, 'w')

        texto = arquivoLeitura.readlines()
        conteudo = ""

        for frase in texto:
            if frase[0] != '#' and frase != "":
                conteudo += frase

        arquivoCopia.write(conteudo)
        arquivoLeitura.close()
        arquivoCopia.close()
    except:
        print("Erro tentar manipular o arquivo")

copiarArquivo("arquivos/Ex01.txt", "arquivos/CopiaEx01.txt")