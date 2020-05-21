import random
class Asteroide:
    def __init__(asteroide):
        asteroide.x = 0
        asteroide.y = 0
        asteroide.raio = 0



    def imprimeValores(asteroide):
        print("posição x", asteroide.x, "posição y", asteroide.y, "raio", asteroide.raio)

    def PosRaioRamdom(asteroide,telaX,telaY):
        asteroide.raio = random.randint(1, 40)
        asteroide.x = random.randint(asteroide.raio*2,telaX-asteroide.raio*2)
        asteroide.y = random.randint(asteroide.raio*2,telaY-asteroide.raio*2)

    def lista(asteroide):
        asteroide1 = Asteroide()
        asteroide2 = Asteroide()
        asteroide3 = Asteroide()
        asteroide4 = Asteroide()
        asteroide5 = Asteroide()
        listaAsteroide = {asteroide1, asteroide2, asteroide3, asteroide4, asteroide5}
        return listaAsteroide

    def cores(asteroide):
        #BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        SPREENGGREEN = (0, 255, 127)
        INDIGO = (75, 0, 130)
        listaCores = {WHITE, GREEN, RED, SPREENGGREEN, INDIGO}
        return listaCores