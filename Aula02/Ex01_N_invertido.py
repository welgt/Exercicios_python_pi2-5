cont = 1
mult = 0
casa = 10

valorUsuario = int(input())

while cont <=3:

    if cont==1:
        resto = valorUsuario % casa  # 10
        print('{:.0f}'.format(resto))
        cont = cont + 1
    resto = valorUsuario % (casa * casa) / casa  # 100
    print('{:.0f}'.format(resto))

    casa = casa*10
    cont = cont+1