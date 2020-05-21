'''
2) Dado um inteiro não-negativo n, faça uma função que calcule e retorne n!
lembrando que n! = n(n−1)*(n−2)*. . . 1 e que 0! = 1).
'''

n = int(input('Informe o numero:\n'))

i = 1
s = 0
j = 0


while i <2:
#r = n*(n-1)*(n-2)*(n-3)*(n-4)

    r = n*(n-i)
    s+=r
    i+=1

print(s)
print('Não deu tempo de terminar esse:(')