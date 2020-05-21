
'''
ENVIADO:
def achaCaracter(str, crt):
    i = 0

    while i < len(str):

        if str[i] == crt:
            print('O caracter ', crt, 'foi encontrado na posicao ', i + 1)
        i += 1

str = str(input('Informe uma palavra:\n'))
crt = input('Informe o caracter de pesquisa:\n')

achaCaracter(str,crt)
'''

# REFATORADO:

def achaCaracter(str, crt):
    i = 0

    while i < len(str):

        if str[i] == crt:
            print('O caracter ', crt, 'foi encontrado na posicao ', i + 1)
        i += 1

str = str(input('Informe uma palavra:\n'))
crt = input('Informe o caracter de pesquisa:\n')

achaCaracter(str,crt)





