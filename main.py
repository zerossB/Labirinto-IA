import time

import numpy as np
from PIL import Image

import base.funcoes as fn
from base.grafo import Graph_state
from base.buscas import BuscaLargura, BuscaProfundidade


def main():
    t0 = time.time()

    #img_data = load_image('4 by 4 orthogonal maze.png')
    img_data = fn.load_image('labirintos/labirinto.png')
    #img_data = load_image('100 by 100 orthogonal maze.png')

    l_entrada, c_entrada = fn.find_entry(img_data)
    lex, cex = fn.find_exit(img_data)
    objective = (lex, cex)
    print("entrada: ", l_entrada, c_entrada)
    print("saida: ", objective, "\n")

    start_point = Graph_state(l_entrada, c_entrada, True)
    start_point.isgoal(objective)

    fn.find_next_intersection(img_data, start_point, fn.find_dir(
        img_data, l_entrada, c_entrada), objective)

    buscaLargura = BuscaLargura()
    resultado = buscaLargura.search(img_data, start_point)
    print(resultado)

    buscaProfundidade = BuscaProfundidade()
    resultado = buscaProfundidade.search(img_data, start_point)
    # print(resultado)

if __name__ == '__main__':
    main()
