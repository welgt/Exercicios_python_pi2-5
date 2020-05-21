from Aula06.Asteroide import *
import pygame

pygame.init()
resolucao = 800, 600
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Registros, instanciar e desenhar o registro")

'''BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SPREENGGREEN = (0, 255, 127)
INDIGO = (75, 0, 130)'''

# asteroid = Asteroide(400,300,30)
'''asteroide1 = Asteroide()
asteroide2 = Asteroide()
asteroide3 = Asteroide()
asteroide4 = Asteroide()
asteroide5 = Asteroide()'''
'''listaAsteroide = {asteroide1, asteroide2, asteroide3, asteroide4, asteroide5}'''

asteroides = Asteroide.lista(Asteroide)

'''listaCores = {BLACK, WHITE, GREEN, RED, SPREENGGREEN, INDIGO}'''
cores = Asteroide.cores(Asteroide)

velocidadeX = 0
velocidadeY = 0

clock = pygame.time.Clock()
jogoAtivo = True
while jogoAtivo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogoAtivo = False

            elif event.key == pygame.K_LEFT:
                velocidadeX -= 10
            elif event.key == pygame.K_RIGHT:
                velocidadeX += 10
            elif event.key == pygame.K_UP:
                velocidadeY -= 10
            elif event.key == pygame.K_DOWN:
                velocidadeY += 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                velocidadeX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                velocidadeY = 0

    # asteroid.x += velocidadeX
    # asteroid.y += velocidadeY

    tela.fill(0)

    # pygame.draw.circle(tela,WHITE,(asteroid.x,asteroid.y),asteroid.raio)

    for asteroide in asteroides:
        for cor in cores:
            asteroide.PosRaioRamdom(resolucao[0], resolucao[1])
            pygame.draw.circle(tela, cor, (asteroide.x, asteroide.y), asteroide.raio)
        clock.tick(10)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

''' asteroide1.PosRaioRamdom(800, 600)
    asteroide2.PosRaioRamdom(800, 600)
    pygame.draw.circle(tela, WHITE, (asteroide1.x, asteroide1.y), asteroide1.raio)
    pygame.draw.circle(tela, WHITE, (asteroide2.x, asteroide2.y), asteroide2.raio)'''