import sys

from PIL import Image

from base.bases import buscaLargura, buscaProfundidade
from base.functions import getInicioEFim, geraResolucao, loadImages


def main():
    # base_image = Image.open(sys.argv[1])
    base_image, base_pixels = loadImages("labirintos/labirinto.png")

    inicio, fim = getInicioEFim(base_image, base_pixels)

    path = buscaLargura(inicio, fim, base_pixels)
    geraResolucao(path, "Largura")

    base_image, base_pixels = loadImages("labirintos/labirinto.png")
    path = buscaProfundidade(inicio, fim, base_pixels)
    geraResolucao(path, "Profundidade", True)


if __name__ == '__main__':
    # https://stackoverflow.com/a/13174351
    main()
