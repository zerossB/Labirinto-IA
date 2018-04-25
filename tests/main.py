from PIL import Image


from base.functions import loadImages, isPreto, getInicioEFim
from base.grafo import Linha


class Quadrado(object):
    def __init__(self, x_ini, y_ini):
        self.dsX = 0
        self.dsY = 0

        self.diX = x_ini + 1
        self.diY = y_ini

        self.esX = 0
        self.esY = 0

        self.eiX = x_ini
        self.eiY = y_ini

    def isNode(self, pixels):
        count = 0

        if isPreto(pixels[self.esX, self.esY]) and isPreto(pixels[self.dsX, self.dsY]):
            #Cima
            pass

        if isPreto(pixels[self.eiX, self.eiY]) and isPreto(pixels[self.diX, self.diY]):
            #Baixo
            pass

    def moveCima(self, move=-1):
        self.diX = self.dsX
        self.eiX = self.esX

        self.diY = self.dsY
        self.eiY = self.esY

        self.dsY = self.dsY + move
        self.esY = self.esY + move

    def moveDireita(self, move=1):
        self.esY = self.dsY
        self.eiY = self.diY

        self.esX = self.dsX
        self.eiX = self.diX

        self.dsX = self.dsX + move
        self.diX = self.diX + move

    def moveEsquerda(self, move=-1):
        self.dsY = self.esY
        self.diY = self.eiY

        self.dsX = self.esX
        self.diX = self.eiX

        self.esX = self.esX + move
        self.eiX = self.eiX + move

    def moveBaixo(self, move=1):
        self.dsX = self.diX
        self.esX = self.eiX

        self.dsY = self.diY
        self.esY = self.eiY

        self.diY = self.diY + move
        self.eiY = self.eiY + move

    def __str__(self):
        print("Ds ", self.dsX, self.dsY)
        print("Di ", self.diX, self.diY)
        print("Es ", self.esX, self.esY)
        print("Ei ", self.eiX, self.eiY, "\n")
        return ""


def main():
    base, pixels = loadImages('./labirintos/labirinto.png')
    incio, fim = getInicioEFim(base, pixels)

    base = Quadrado(incio[0], incio[1])
    str(base)

    count = 1

    while isPreto(pixels[base.eiX, base.eiY]) and isPreto(pixels[base.diX, base.diY]):
        base.moveBaixo()
        str(base)
        count = count + 1

    print("Contador: ", count)


if __name__ == '__main__':
    main()
