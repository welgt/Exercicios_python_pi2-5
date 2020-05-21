import pygame

pygame.init()

resolucao = 800,600
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Animacao de imagem")

BLACK = ( 0, 0, 0)

player = pygame.image.load("arquivos/lunarlander.png")
rect_player = player.get_rect()
posX = resolucao[0]/2 - 50/2
posY = resolucao[1]/2 - 86/2

angulo = -90
clork = pygame.time.Clock()

def rotCentroGeral(image, rect, angle, posX, posY):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    rot_rect[0]+=posX
    rot_rect[1]+=posY
    return rot_image,rot_rect

jogoAtivo = True

while jogoAtivo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jogoAtivo = False

    tela.fill(BLACK)
    rotacao = rotCentroGeral(player, rect_player, angulo, posX, posY)
    player = pygame.transform.rotate(player,angulo)
    #tela.blit(player, (posX,posY))
    tela.blit(rotacao[0],rotacao[1])
    pygame.display.flip()
    clork.tick(30)

pygame.quit()