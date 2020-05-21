t = int(input('Informe o tamanho do triangulo:\n'))
i = 0
j = 0

while t>0:
    while i<t:
        print(i, end=" ")
        i+=1
    print()
    t-=1
    i= 0
