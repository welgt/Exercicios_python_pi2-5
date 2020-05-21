
sair = False
while not sair:
    opcao = int(input('Aperte \n1 para instrucoes\n2 para jogar e \n3 para sair\n'))
    if opcao == 1:
        print('Voce entrou nas instrucoes do game')

    elif opcao == 2:
        print('Voce esta jogando')

    elif opcao == 3:
        print('Voce quitou!')
        sair = True

    else:
        print('Fudeu')