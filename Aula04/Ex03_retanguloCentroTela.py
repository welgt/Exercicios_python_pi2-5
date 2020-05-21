import pygame

larguraTela = int(input('Informe a largura e altura da tela:\n'))
alturaTela =  int(input())

resolucao = (larguraTela,alturaTela)
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)

largura  = 100
altura = 200

posX = (larguraTela/2) - (largura/2)
posY = (alturaTela/2) - (altura/2)

retangulo = (posX,posY,largura,altura)

tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption('Retangulo no centro da tela')

tela.fill(RED)

jogoAtivo = True

while jogoAtivo:
    for evento in pygame.event.get():

        pygame.draw.rect(tela, WHITE, retangulo)
        pygame.display.flip()
        if evento.type == pygame.QUIT:
            jogoAtivo = False

pygame.quit()