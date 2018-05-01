from base.funcoes import addQueue
from queue import Queue, LifoQueue
import numpy as np


def buscaLargura(data, estado_pai, objective):
    queue = Queue()
    queue.put(estado_pai)  # Envolvendo a tupla inicial em uma lista

    full_path = list()
    marcado = []

    count = 1

    while not queue.empty():
        path = queue.get()

        marcado.append(path)

        # Se eu cheguei no final, retorno o caminho
        if path.goal:
            return path, count, full_path

        for adjacente in path.children:
            x = adjacente.column
            y = adjacente.line
            full_path.append(adjacente)

            if not adjacente in marcado:
                print(" ", x, y)
                queue.put(adjacente)
            
        count = count + 1
    print("A fila esgotou-se. Nenhuma resposta foi encontrada.")
