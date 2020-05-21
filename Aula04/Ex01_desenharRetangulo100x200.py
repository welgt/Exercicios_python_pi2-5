import pygame

titulo = "Apresentar retangulo no canto da tela"
resolucaoTela = 600, 400

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

larguraRetangulo = 100
alturaRetangulo = 200

posXretangulo = 0
posYretangulo = 0

retangulo = pygame.Rect(posXretangulo, posYretangulo, larguraRetangulo, alturaRetangulo)

tela = pygame.display.set_mode(resolucaoTela)
pygame.display.set_caption(titulo)

tela.fill(WHITE)


jogoAtivo = True
while jogoAtivo:
    for evento in pygame.event.get():

        pygame.draw.rect(tela,BLACK,retangulo)
        pygame.display.flip()
        if evento.type == pygame.QUIT:
            jogoAtivo = False

pygame.quit()


#pygame.display.flip(): Atualiza a surface principal da janela
#screen.fill((255,255,255)) para limpar tela com determinada cor
#pygame.display.flip(). Após mudar a cor da surface é necessário atualizá-la
#pygame.time.delay(1000) tempo para fechar a tela
# pygame.display.flip() limpa os desenhos da tela




