
def uniao(a,b):
    c = ['*'] * (len(a) + len(b))

    resp = ""
    j = 0

    for A in a:
        resp += str(A)

        while j < len(b):
            if a[j] == b[j]:
                j += 1
                resp = resp + str(b[j])
            j += 1

    print(resp)

a = [7, 2, 5, 8, 4]
b = [4, 2, 9, 5]

uniao(a,b)




#C = a ∪ b = [7, 2, 5, 8, 4, 9]
'''
a = [7, 2, 5, 8, 4]
b = [4, 2, 9, 5]
c = ['*']*(len(a)+len(b))
i = 0

for A in a:
    for B in b:
        if A != B:
            c[i] = A
    if c[i] != '*':
        print(c[i], end=" ")
    i+=1
'''









#print(resp)