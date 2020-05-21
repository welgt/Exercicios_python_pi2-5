sair =  False

while not sair:
    reposta = input("Voce quer sair? (s/n)")
    if reposta == 's':
        sair = True
    else:
        atacar = input('Será que seu elfo pode atacar 0 dragao? (s/n)')
        if atacar == 's':
            print('Péssima escolha, voce morreu.')
            sair = True
