import pygame

# Define cores
PRETO = (0, 0, 0)
BRANCO = [255, 255, 255]

tamanho_da_tela = [400, 400]  # largura e altura

screen = pygame.display.set_mode(tamanho_da_tela)
pygame.display.set_caption("exercicio sprites")

princesa = pygame.image.load("sprites/yasuko_sheet.png")

jogo_ativo = True

clock = pygame.time.Clock()  # define o clock para limitar o fps do jogo

x_da_imagem = 77
y_da_imagem = 0
largura_da_imagem = 19

while jogo_ativo:
    for event in pygame.event.get():  # usuario fez algo
        if event.type == pygame.QUIT:  # se usuario apertou para sair
            jogo_ativo = False  # muda a variavel para interromper o laco

    screen.fill(PRETO)  # limpa a tela com cor preta

    screen.blit(princesa,[10,10],[x_da_imagem,y_da_imagem,largura_da_imagem,35])

    x_da_imagem = x_da_imagem + largura_da_imagem

    if x_da_imagem > largura_da_imagem * 6:
        x_da_imagem = 77


    pygame.display.flip()  # manda todos os desenhos para a tela
    clock.tick(5)  # clock limitado para este laco, no caso game loop
pygame.quit()