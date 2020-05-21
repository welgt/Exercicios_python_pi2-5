import pygame

def colisao(posEixoObjeto, tamanhoObjeto, resolucaoTela):
    if posEixoObjeto >= 0 and posEixoObjeto <= resolucaoTela - tamanhoObjeto:
        print('livre')
    else:
        print('Colidiu')
        if posEixoObjeto < resolucaoTela / 2:
            posEixoObjeto = 0
        else:
            posEixoObjeto = resolucaoTela - tamanhoObjeto
    return posEixoObjeto

larguraTela = int(input('Informe a largura e a altura da tela: \n'))
alturaTela = int(input())

pygame.init()
resolucao = ((larguraTela,alturaTela))
tela = pygame.display.set_mode((resolucao))
pygame.display.set_caption('Mover retangulo com colisao e tela redimensionavel')


velx = 2
vely = 2

tamRetanguloX = 80
tamRetanguloY = 150

posRetangulo_x = (larguraTela / 2) - (tamRetanguloX / 2)
posRetangulo_y = (alturaTela / 2) - (tamRetanguloY / 2)

SPREENGGREEN = (0, 255, 127)
INDIGO = (75,0,130)

clock = pygame.time.Clock()
fps = 60

velocodadeTempX = 0
velocidadeTempY = 0
jogoAtivo = True

while jogoAtivo:

    tela.fill(SPREENGGREEN)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jogoAtivo = False

            # controle
            if evento.key == pygame.K_UP:
                velocidadeTempY = -vely
            if evento.key == pygame.K_DOWN:
                velocidadeTempY = vely

            if evento.key == pygame.K_LEFT:
                velocodadeTempX = -velx
            if evento.key == pygame.K_RIGHT:
                velocodadeTempX = velx

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                velocodadeTempX = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                velocidadeTempY = 0

    posRetangulo_x = colisao(posRetangulo_x, tamRetanguloX, resolucao[0])
    posRetangulo_y = colisao(posRetangulo_y, tamRetanguloY, resolucao[1])

    posRetangulo_x += velocodadeTempX
    posRetangulo_y += velocidadeTempY

    retangulo = (posRetangulo_x, posRetangulo_y, tamRetanguloX, tamRetanguloY)
    pygame.draw.rect(tela, INDIGO, retangulo)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()