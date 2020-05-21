
def vericicaIgualdade(str):
    i = 0
    t = len(str) - 1

    while i < t and i <= t / 2:
        if str[i] != str[t - i]:
            return False
        else:
            return True
        i += 1

st = str(input('Escreva uma palavra:\n'))
print(vericicaIgualdade(st))