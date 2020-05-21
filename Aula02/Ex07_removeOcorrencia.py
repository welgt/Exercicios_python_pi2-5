
'''# VERSAO MINHA REFATORADA APOS ENVIO
def achaCaracter(str, crt):
    i = 0
    j = 0

    vetAux = [len(str)]
    while i < len(str):

        if str[i] == crt:
         #   print()
            i+=1
        #print(str[i])
        vetAux[j] = str[i]

        i += 1
        print(vetAux[j], end="")

str = str(input('Informe uma palavra:\n'))
crt = input('Informe o caracter para remover:\n')
str = achaCaracter(str,crt)
'''

# VERSAO MINHA REFATORADA APOS ENVIO

def achaCaracter(str, crt):
    i = 0
    j = 0

    Aux = len(str)
    while i < len(str)-1:

        if str[i] == crt:
         #   print()
            i+=1
        #print(str[i])
        Aux = str[i]

        i += 1
        print(Aux, end="")

str = str(input('Informe uma palavra:\n'))
crt = input('Informe o caracter para remover:\n')
str = achaCaracter(str,crt)




