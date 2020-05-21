'''
A=[ 1, 3, 6, 7] e B=[2, 4, 5]
a nova lista C é feita a partir da INTERCALAÇÃO de A e B:
C=[1, 2, 3, 5, 6, 7]
'''

a=[ 1, 3, 6, 7]
b=[2, 4, 5]
c = ['*'] * (len(a) + len(b))

i = 0
for A in a:
    c[i] = A
    i+=1

j = len(a)
for B in b:
    c[j] = B
    j+=1

c.sort()
print(c)