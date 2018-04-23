import sys

from PIL import Image

from base.bases import buscaLargura, buscaProfundidade
from base.functions import getInicioEFim, geraResolucao, loadImages


def main():
    # base_image = Image.open(sys.argv[1])
    base_image, base_pixels = loadImages("labirintos/labirinto.png")

    inicio, fim = getInicioEFim(base_image, base_pixels)

    path, full_path = buscaLargura(inicio, fim, base_pixels)
    geraResolucao(path, "Largura", full_path, True)

    base_image, base_pixels = loadImages("labirintos/labirinto.png")
    path, full_path = buscaProfundidade(inicio, fim, base_pixels)
    geraResolucao(path, "Profundidade", full_path, True)


if __name__ == '__main__':
    # https://stackoverflow.com/a/13174351
    main()
