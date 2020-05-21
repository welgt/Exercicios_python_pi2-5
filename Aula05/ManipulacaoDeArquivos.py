def copiarArquivo(arquivo1, arquivo2):
    f1 = open(arquivo1, 'r')
    f2 = open(arquivo2, 'w')
    terminou = False
    while not terminou:
        texto = f1.readline()
        if texto == "":
            terminou = True
        f2.write(texto)
    f1.close()
    f2.close()

copiarArquivo("teste.txt", "CopiaDoTeste.txt")