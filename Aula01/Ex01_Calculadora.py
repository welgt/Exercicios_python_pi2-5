
operacao = ['+','-','*','/','x']
tipoOperacao = '"'

sair = False

while not sair:

    n1 = float(input('Informe o primeiro numero:\n'))
    tipoOperacao = str(input('Informe a operação:\n'))

    n2 = float(input('Informe o segundo numero:\n'))

    if tipoOperacao[0] == operacao[0]:
        s = n1 + n2
        print('= {:.0f}'.format(s))

    if tipoOperacao[0] == operacao[1]:
        s = n1 - n2
        print('= {:.0f}'.format(s))

    if tipoOperacao[0] == operacao[2]:
        s = n1 * n2
        print('= {:.0f}'.format(s))

    if tipoOperacao[0] == operacao[3]:
        s = n1 / n2
        print('= {:.0f}'.format(s))

    exit = str(input('para continuar aperte s\npara sair aperte n'))
    if exit == "n":
        sair = True
