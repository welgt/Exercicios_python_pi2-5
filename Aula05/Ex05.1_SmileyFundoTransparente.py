import pygame

pygame.init()

resolucao = 800,600
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)



tela = pygame.display.set_mode((resolucao))
pygame.display.set_caption("Mudar o fundo da imagem do Smiley para transparente")
tela.fill(RED)

smiley = pygame.image.load("arquivos/smiley.bmp")
#cor_transp = smiley.get_at((0,0))
#smiley.set_colorkey(cor_transp)
#smiley = smiley.convert()


jogoAtivo = True

while jogoAtivo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key ==pygame.K_ESCAPE:
                jogoAtivo = False

        tela.blit(smiley,(250,150))
        pygame.display.flip()

pygame.quit()