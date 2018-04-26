from PIL import Image


from base.functions import loadImages, isPreto, getInicioEFim


class Quadrado(object):

    def __init__(self, x_ini, y_ini):
        self.passei = False

        self.dsX = 0
        self.dsY = 0

        self.diX = x_ini + 1
        self.diY = y_ini

        self.esX = 0
        self.esY = 0

        self.eiX = x_ini
        self.eiY = y_ini

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


def mapMaze(self, pixels):
    path = []


def main():
    base, pixels = loadImages('./labirintos/labirinto.png')
    inicio, fim = getInicioEFim(base, pixels)

    graph = Quadrado(inicio[0], inicio[1])

    pretos = []

    for x in range(0, base.width):
        for y in range(0, base.height):
            if isPreto(pixels[x, y]):
                pretos.append((x, y))

    count = 0
    pixel_1 = pretos[0]
    pixel_2 = pretos[1]

    # while isPreto(pixels[graph.eiX, graph.eiY]) and isPreto(pixels[graph.diX, graph.diY]):
    #     graph.moveBaixo()
    #     str(graph)
    #     count = count + 1

    # print("Contador: ", count)


if __name__ == '__main__':
    main()
