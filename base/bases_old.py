"""
    Arquivo para construir toda as nossas funções de buscas
"""
import time

from queue import Queue, LifoQueue
from .functions import isPreto, getAdjacentes, printSpecs, addQueue


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

    #'cria uma fila vazia que recebe um "LIFO"'
    queue = LifoQueue()

    #'Starta a fila vazia'
    queue.put([start])

    #'Inicia lista vazia e começa a contagem a partir do 1 que seria o elemento pai'    
    full_path = list()
    count = 1

    #'Enquanto a fila não for vazia'
    while not queue.empty():
        #'Remover item da fila'
        path = queue.get()

        # print(pixel)

        #'Verifica se o último item for um pixel'
        if pixel == end:
            #'retornar esse item, quantidade de grafos analisados e a lista cheia'
            return path, count, full_path

        #'Para adjacente dentro de ObterAdjacente(parâmetro{pixel})'
        for adjacente in getAdjacentes(pixel):
            #'X e Y são adjacentes'
            x, y = adjacente

            #'Acrescentar Adjacentes X e Y na lista vazia'
            full_path.append(adjacente)

            #'Tentar'
            try:
                #'Se pixel é preto nos adjacentes X e Y'
                if isPreto(pixels[x, y]):
                    # print(" ", x, y)
                    ''
                    pixels[x, y] = (0, 255, 0, 255)
                    queue.put(addQueue(path, adjacente))
            except IndexError:
                pass
        count = count + 1
    print("A pilha esgotou-se. Nenhuma resposta foi encontrada.")


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

    full_path = list()

    count = 1

    while not queue.empty():
        path = queue.get()
        pixel = path[-1]

        # Se eu cheguei no final, retorno o caminho
        if pixel == end:
            return path, count, full_path

        for adjacente in getAdjacentes(pixel):
            x, y = adjacente

            full_path.append(adjacente)

            try:
                if isPreto(pixels[x, y]):
                    # print(" ", x, y)
                    queue.put(addQueue(path, adjacente))
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
    path, count, full_path = buscaEmProfundidade(inicio, fim, base)
    t_fim = time.time()

    printSpecs(t_ini, t_fim, "Largura", path, count, full_path)

    return path, full_path


def buscaLargura(inicio, fim, base):
    print("\n\nIniciando Busca em Largura")
    t_ini = time.time()
    path, count, full_path = buscaEmLargura(inicio, fim, base)
    t_fim = time.time()

    printSpecs(t_ini, t_fim, "Largura", path, count, full_path)

    return path, full_path
