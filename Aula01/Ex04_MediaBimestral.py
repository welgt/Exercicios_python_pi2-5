n1 = float(input('Informe 4 notas:\n'))
n2 = float(input())
n3 = float(input())
n4 = float(input())

media = (n1+n2+n3+n4)/4

if media>10:
    media = 10
print('A media é: {:.01f}'.format(media))