#Exercício 1
x = int(input("digite um número maior que zero"))

reverso_x = 0

while x>0:
    Digito = x%10
    reverso_x = (reverso_x*10)+Digito
    x=int(x/10)


print("numero invertido: ",reverso_x)

#Exercício 2
x = int(input("digite um número maior que zero"))

resultado=1
count=1

while count <= x:
    resultado *= count
    count += 1

print(resultado)

#Exercício 3
n = int(input("digite até que termo deseja encontrar"))

ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    print("1")
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)

#Exercício 4
n = int(input("digite um número"))

resultado = str(n%2)
n = int(n / 2)
while n > 0:
    resultado = str(n%2) + resultado
    n = int(n / 2)
print(resultado)

#Exercício 5
palindrome =input("digite uma palavra para saber se é palindrome ")

stringInvertida = palindrome[::-1] #[::-1] inverte uma string
if stringInvertida == palindrome:
    print ("SIM")
else:
    print ("NAO")


#Exercício 6
def conta(string, caractere):
    contador=0
    for letra in string:
        if letra == caractere: contador=contador+1
    return contador

palavra = input("digite uma palavra")
letra = input("digite uma letra")
print("a quantidade de letra na palavra eh: ", conta(palavra,letra))


#Exercício 7
def removerLetras(palavra, letra):
    novapalavra = ''
    for caractere in palavra:
        if caractere != letra:
            novapalavra=novapalavra+caractere
    return novapalavra

palavra = input("digite uma palavra")
letra = input("digite uma letra")
print("a quantidade de letra na palavra eh: ", removerLetras(palavra,letra))

#Exercício 8
x = int(input("digite um número: "))

while x > 0:
    print(list(range(x)))
    x=x-1