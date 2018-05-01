from base.funcoes import addQueue
from queue import Queue, LifoQueue
import numpy as np
import base.funcoes as fn


def buscaLargura(data, estado_pai):
    cor = {}
    pred = {}
    d = {}

    for v in fn.list_state(estado_pai, []):
        d[v] = np.inf
        cor[v] = 'branco'  # branco cinza e preto
        pred[v] = None

    cor[estado_pai] = 'cinza'
    d[estado_pai] = 0

    Q = Queue()
    Q.put(estado_pai)

    while not Q.empty():
        u = Q.get()

        if u.goal:
            return pred

        for v in u.children:
            if cor[v] == 'branco':
                cor[v] = 'cinza'
                d[v] = d[u] + 1
                pred[v] = u

                Q.put(v)
        cor[u] = 'preto'


def buscaProfundidade(data, estado_pai):
    cor = {}
    pred = {}
    d = {}

    for v in fn.list_state(estado_pai, []):
        d[v] = np.inf
        cor[v] = 'branco'  # branco cinza e preto
        pred[v] = None

    cor[estado_pai] = 'cinza'
    d[estado_pai] = 0

    Q = LifoQueue()
    Q.put(estado_pai)

    while not Q.empty():
        u = Q.get()

        if u.goal:
            return pred

        for v in u.children:
            if cor[v] == 'branco':
                cor[v] = 'cinza'
                d[v] = d[u] + 1
                pred[v] = u

                Q.put(v)
        cor[u] = 'preto'

    return pred
