# LunarLander2d.py
# Copyright Warren Sande, 2011

# Baseado no LunarLander, Copyright Warren Sande, 2009 # Lançado sob licença do MIT http://www.opensource.org/licenses/mit-license.php

# LunarLander 2D
# jogo de simulação de pouso de uma nave espacial

"""O LunarLander original em" Olá Mundo! A programação de computadores para crianças e outros iniciantes "era uma versão muito simples em 1-D (eixo Y, apenas com movimento vertical) do Lunar Lander, apenas para demonstrar uma simulação de simplicidade de gravação usando o Pygame.

O LunarLander 2D adiciona o eixo x (movimento lateral). Agora você pode girar o lander usando as teclas de seta para a direita / esquerda, mais como a versão arcade original. Também altera o controle de empuxo de baseado no mouse (arrastando o controle deslizante) para baseado no teclado (mantenha pressionada a barra de espaço).

Em vez da imagem da superfície lunar, ela usa um retângulo simples da plataforma de aterrissagem.

"""

# initialize - prepare tudo
import pygame, sys
from math import *
pygame.init()
# tela mais larga que o LunarLander, já que temos movimentos laterais
screen = pygame.display.set_mode([800,600])
screen.fill([0, 0, 0])
ground  = 540   #landing pad é sim
y = 540
start = 90      # localização inicial a 90 pixels da parte superior da janela
clock = pygame.time.Clock()
ship_mass = 5000.0
combustivel = 5000.0
fps = 30
delta_v = 0

#defaultx_loc = 20 # x-localização em metros = distância do centro da pista de pouso
x_loc = 20
y_loc = 40  # y-localização em metros = altura acima da plataforma de aterrissagem

x_offset = 40    # deslocamentos para que, quando a localização do navio for (0,0), o navio seja
y_offset = -108  # apenas tocando na plataforma de aterrissagem e centralizado.

x_speed = 2000.0   # pixels / framey_speed = -800.0
y_speed = -800.0


x_velocity = x_speed / (10.0 * fps)  # m/s
y_velocity = y_speed / (10.0 * fps)

gravity = 1.5
impulso = 0

scale = 10   #scale factor de pixels em metros
acelerar_baixo = False
esquerda_baixo = False
direita_baixo = False
mantido_baixo = False
count = 0
x_pos = 0
y_pos = 0

"""x_pos, y_pos em pixels - (0,0) é superior esquerdox_loc, y_loc em metros - (0,0) é o centro da área de pouso

x_speed, y_speed em pixels por quadro.x_velocity, y_velocity em m / s

fator de escala = 10 (10 pixels = 1 metro)

pos (pixels) para local (metros) é dimensionado por: scaleFactor (metros / pixel) velocidade (pixels / quadro) para velocidade (m / s) é dimensionado por: ScaleFactor * FPS (quadros por segundo)

"""

# sprite para a classe da nave
class ShipClass(pygame.sprite.Sprite):
  def __init__(self, image_file, position):

      pygame.sprite.Sprite.__init__(self)
      self.imageMaster = pygame.image.load(image_file)
      self.image = self.imageMaster
      self.rect = self.image.get_rect()
      self.position = position
      self.rect.centerx, self.rect.centery = self.position
      self.angle = 0

  def update(self):
      self.rect.centerx, self.rect.centery = self.position
      oldCenter = self.rect.center
      self.image = pygame.transform.rotate(self.imageMaster, self.angle)
      self.rect = self.image.get_rect()
      self.rect.center = oldCenter

# posição do calcualte, movimento, aceleração, combustível
def calculate_velocity():
  global ship, impulso, combustivel, x_velocity, y_velocity, x_loc, y_loc
  global tot_velocity, scale, x_pos, y_pos, x_speed, y_speed

  delta_t = 1/fps

  # Calcular impulso com base na barra de espaço sendo mantida pressionada
  if acelerar_baixo:
      impulso = impulso + 100
      if impulso > 1000:
          impulso = 1000
  else:
      if impulso > 0:
          impulso = impulso - 200
          if impulso < 0:
              impulso = 0
  combustivel -= impulso / (10 * fps)  # use up fuel
  if combustivel < 0:
    combustivel = 0.0
  if combustivel < 0.1:
    impulso = 0.0


  ythrust = impulso * cos(ship.angle * (pi / 180))
  xthrust = impulso * sin(ship.angle * (pi / 180))
  y_delta_v = delta_t * (-gravity + 50 * ythrust / (ship_mass + combustivel))
  y_velocity = y_velocity + y_delta_v
  x_delta_v = delta_t * (-50 * xthrust / (ship_mass + combustivel))
  x_velocity = x_velocity + x_delta_v
  x_speed = x_velocity * 10.0/fps   # velocidade em pixels / quadro, velocidade em m / s
  y_speed = y_velocity * 10.0/fps
  y_loc = y_loc + y_velocity/fps    # local em metros, velocidade em m / s
  x_loc = x_loc - x_velocity/fps
  #tot_velocity = sqrt(x_velocity**2 + y_velocity**2)
  ship.position[0] = x_pos = screen.get_width()/2 - (scale * x_loc) + x_offset
  ship.position[1] = y_pos = screen.get_height() - (scale * y_loc) + y_offset

  if direita_baixo:
      ship.angle = ship.angle - 2
  if esquerda_baixo:
      ship.angle = ship.angle + 2
  ship.update()


# criar uma instância do sprite do nave
ship = ShipClass('lunarlander.png', [500, 230])

# main loop
while True:


  clock.tick(30)
  fps = clock.get_fps()
  if fps < 1:
       fps = 30
  count += 1
  if y_loc > 0.01:
      calculate_velocity()
      screen.fill([0, 0, 0])
      screen.blit(ship.image, ship.rect)
      pygame.display.flip()


  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              acelerar_baixo = True
          if event.key == pygame.K_RIGHT:
              direita_baixo = True
          if event.key == pygame.K_LEFT:
              esquerda_baixo = True
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_SPACE:
              acelerar_baixo = False
          if event.key == pygame.K_RIGHT:
              direita_baixo = False
          if event.key == pygame.K_LEFT:
              esquerda_baixo = False