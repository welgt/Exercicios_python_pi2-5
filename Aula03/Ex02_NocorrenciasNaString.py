str = str(input('Informe uma palavra:\n'))
i = 0

while i < len(str):
    print('A letra', str[i] + ' apareceu ', str.count(str[i]), ' vez.' )
    i += 1
