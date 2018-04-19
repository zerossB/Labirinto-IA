"""
    Arquivo para construir toda as nossas funções de buscas
"""
import time

from queue import Queue, LifoQueue
from .functions import isPreto, getAdjacentes, printSpecs


def buscaEmProfundidade(start, end, pixels):
    """
        Faz a busca em largura
        Crio uma pilha, e adiciono o primeiro item nela (no caso o começo do labirinto)

        Enquanto a pilha não for vazia vou percorrer ela, verificando se o pixel que estou,
            não é o final do labirinto
        Procuro os adjacentes a partir do pixel atual
        Se ele for preto, coloco ele dentro de uma pilha, e dessa pilha coloco ele na na minha queue

        Fazendo assim, o percorrer do labirinto
    """
    queue = LifoQueue()
    queue.put([start])

    count = 1

    while not queue.empty():
        path = queue.get()
        pixel = path[-1]

        # print(pixel)

        if pixel == end:
            return path, count

        for adjacente in getAdjacentes(pixel):
            x, y = adjacente
            try:
                if isPreto(pixels[x, y]):
                    #print(" ", x, y)
                    pixels[x, y] = (0, 255, 0, 255)
                    novo_path = list(path)
                    novo_path.append(adjacente)
                    queue.put(novo_path)
            except IndexError:
                pass
        count = count + 1
    print("A fila esgotou-se. Nenhuma resposta foi encontrada.")


def buscaEmLargura(start, end, pixels):
    """
        Faz a busca em largura
        Crio uma lista, e adiciono o primeiro item nela (no caso o começo do labirinto)

        Enquanto a lista não for vazia vou percorrer ela, verificando se o pixel que estou,
            não é o final do labirinto
        Procuro os adjacentes a partir do pixel atual
        Se ele for preto, coloco ele dentro de uma lista, e dessa lista coloco ele na na minha queue

        Fazendo assim, o percorrer do labirinto
    """
    queue = Queue()
    queue.put([start])  # Envolvendo a tupla inicial em uma lista

    count = 1

    while not queue.empty():
        path = queue.get()
        pixel = path[-1]

        # print(pixel)

        # Se eu cheguei no final, retorno o caminho
        if pixel == end:
            return path, count

        for adjacente in getAdjacentes(pixel):
            x, y = adjacente
            try:
                if isPreto(pixels[x, y]):
                    #print(" ", x, y)
                    pixels[x, y] = (0, 255, 0, 255)
                    novo_path = list(path)
                    novo_path.append(adjacente)
                    queue.put(novo_path)
            except IndexError:
                pass
        count = count + 1
    print("A fila esgotou-se. Nenhuma resposta foi encontrada.")


#
#   Aqui coloca todas as funções p/ calcular tempo, memória e afins...
#


def buscaProfundidade(inicio, fim, base):
    print("\n\nIniciando Busca em Profundidade")
    t_ini = time.time()
    path, count = buscaEmProfundidade(inicio, fim, base)
    t_fim = time.time()

    printSpecs(t_ini, t_fim, "Profundidade", path, count)

    return path


def buscaLargura(inicio, fim, base):
    print("\n\nIniciando Busca em Largura")
    t_ini = time.time()
    path, count = buscaEmLargura(inicio, fim, base)
    t_fim = time.time()

    printSpecs(t_ini, t_fim, "Largura", path, count)

    return path
