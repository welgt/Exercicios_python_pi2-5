import pygame

pygame.init()

resolucao = 800,600
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Animacao de imagem")

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

player = pygame.image.load("arquivos/yasuko_sheet.png")
posX = resolucao[0]/2 - 18/2    #resolucao da imagem cortada
posY = resolucao[1]/2 - 36/2    #resolucao da imagem cortada

posicaoInicialImg = 19
x_da_imagem = posicaoInicialImg
y_da_imagem = 0

larguraRecorte = posicaoInicialImg
alturaRecorte = 36

jogoAtivo = True
clork = pygame.time.Clock()

while jogoAtivo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jogoAtivo = False

    tela.fill(BLACK)

    tela.blit(player, (posX,posY), (x_da_imagem, y_da_imagem, larguraRecorte, alturaRecorte))
    x_da_imagem = x_da_imagem + larguraRecorte

    if x_da_imagem > larguraRecorte*4:
        x_da_imagem = posicaoInicialImg

    pygame.display.flip()
    clork.tick(5)

pygame.quit()