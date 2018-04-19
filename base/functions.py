"""
    Arquivo para funções básicas do Projeto
"""
import sys
import os

from PIL import Image


def loadImages(path_file):
    """
        Carrega imagens do labirinto
    """
    try:
        base_image = Image.open(path_file)
        base_pixels = base_image.load()
        return base_image, base_pixels
    except IOError as io:
        print("O arquivo não pode ser encontrado ou a imagem não pode ser aberta e identificada. \n", io)
        sys.exit(2)


def geraResolucao(path, name, show=False):
    """
        Pego a minha solução e coloco a linha vermelha
            no caminho correto
    """
    #base_image = Image.open(sys.argv[1])
    path_image, path_pixels = loadImages("labirintos/labirinto.png")

    for posicao in path:
        x, y = posicao
        # Pinto o rastro de informações de Vermelho
        path_pixels[x, y] = (255, 0, 0)

    try:
        print("\nPrintando Solução |", name)
        name_file = "Resolucao-"+name+".png"
        path_image.save("resolv/"+name_file)
        #print(os.path.abspath(path_image.filename))
    except (KeyError, IOError) as err:
        print(err)

    if show:
        # path_img.save(sys.argv[2])
        path_image.show()


def isPreto(pixel):
    """
        Verifica se o pixel em questão é preto
    """
    if pixel == (0, 0, 0, 255):
        return True


def getAdjacentes(pixel):
    """
        Retorna todos os adjacentes do pixel atual
        No caso:
        Norte, Sul, Leste e Oeste (Os arredores)
    """
    x, y = pixel
    return [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]


def printSpecs(t_ini, t_fim, busca, path, count):
    """
        Printa informações sobre as funções
    """
    print("\nTempo de Resolução: ", t_fim - t_ini, "ms")
    print("Metodo de Buca: ", busca)
    print("Número de estados Analisados ", count)
    print("Número de estados p/ Solução: ", len(path))
    print("Memória Alocada: ", sys.getsizeof(path), "KBytes")


def getInicioEFim(image, pixels):
    """
        Pesquiso pixel de inicio e pixel de fim do labirinto
    """
    w, h = image.size
    inicio = 0
    fim = 0

    # Pequisando o Primeiro Pixel do Labirinto
    for width in range(0, w-1):
        if isPreto(pixels[width, 1]):
            inicio = width
            break

    # Pequisando o Ultimo Pixel do Labirinto
    for heigth in range(0, w-1):
        if isPreto(pixels[heigth, h-1]):
            fim = heigth
            break

    return (inicio, 1), (fim, h-1)
