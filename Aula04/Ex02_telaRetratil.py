import pygame

larguraTela = int(input('Informe a largura e altura da tela:\n'))
alturaTela = int(input())

resolucao = larguraTela,alturaTela

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)

tela = pygame.display.set_mode(resolucao)
tela.fill(RED)
pygame.display.set_caption('Tela retratil')

posRetanguloX = 0
posRetanguloY = 0

larguraRetangulo = 100
alturaRtangulo = 200
retangulo = pygame.Rect(posRetanguloX, posRetanguloY, larguraRetangulo, alturaRtangulo )

jogoAtivo = True

while jogoAtivo:
    for evento in pygame.event.get():

        pygame.draw.rect(tela, WHITE, retangulo)
        pygame.display.flip()

        if evento.type == pygame.QUIT:
            jogoAtivo = False

pygame.quit()