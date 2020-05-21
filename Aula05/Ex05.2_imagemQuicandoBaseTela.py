import pygame

pygame.init()

def colisao(posObj, tamanhoObj, resolucaoTela):
    if posObj >= 0 and posObj <= resolucaoTela - tamanhoObj:
        print('livre')
    else:
        print('Colidiu')
        if posObj < resolucaoTela / 2:
            posObj = 0
        else:
            posObj = resolucaoTela - tamanhoObj
    return posObj

'''
def quica(posObj,velObj,forcaImpulso):
    if posObj > 340 and velObj>1:
        posObj += (velObj * - forcaImpulso)
        forcaImpulso-=1
        velObj-=0.5
'''

resolucao = 800,600
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

tela = pygame.display.set_mode((resolucao))
pygame.display.set_caption("Mudar o fundo da imagem do Smiley para transparente")
tela.fill(RED)

smiley = pygame.image.load("arquivos/smiley.bmp")

posY = 0
posX = resolucao[0]/2
vel = 4
tamanhoX = 256
tamanhoY = 256

forcaImpulso = 15#20
clock = pygame.time.Clock()
jogoAtivo = True

while jogoAtivo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key ==pygame.K_ESCAPE:
                jogoAtivo = False


    posX = colisao(posX, tamanhoX, resolucao[0])
    posY = colisao(posY,tamanhoY,resolucao[1])


    if posY > 340 and vel>1:
        posY += (vel * - forcaImpulso)
        forcaImpulso-=1
        vel-=0.5

    posY += vel
    tela.blit(smiley, (posX, posY))
    pygame.display.flip()
    tela.fill(RED)

    clock.tick(60)

pygame.quit()