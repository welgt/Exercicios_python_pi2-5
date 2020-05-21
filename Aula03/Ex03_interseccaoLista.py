'''
3) Escreva um função que efetua a INTERSECÇÃO entre duas listas, ou seja, os
elementos em comum entre as duas listas. Considere que as listas não contêm
valores duplicados e não estão ordenadas. Como resultado deve ser gerado uma
nova lista e retornada, a nova lista conterá a INTERSECÇÃO das duas listas, exemplo:
A = [7, 2, 5, 8, 4] e B = [4, 2, 9, 5]
C = A ∩ B = [2, 5, 4]
'''

def interseccao(a,b):
    c = ['*'] * (len(a) + len(b))

    i = 0
    for A in a:
        for B in b:
            if A == B:
                c[i] = B
        if c[i] != '*':
            print(c[i], end=" ")
        i += 1

a = [7, 2, 5, 8, 4]
b = [4, 2, 9, 5]

interseccao(a,b)


'''
a = [7, 2, 5, 8, 4]
b = [4, 2, 9, 5]

i = 0
j = 0

c= [0]*5

resp = ""

while i < len(a):
    while j < len(b):
        if a[i] == b[j]:
            resp = resp + str(a[i])
            #c[i] = a[i]
        j+=1
    i+=1
print(resp)
print(c)
'''