from base.funcoes import addQueue
from queue import Queue, LifoQueue
import numpy as np
import base.funcoes as fn


class Buscas(object):
    def __init__(self):
        self.visitado = []
        self.marcado = []
        self.resultado = []


class BuscaLargura(Buscas):
    def __init__(self):
        super().__init__()

    def search(self, data, estado_pai):
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

        self.resultado = filter(lambda x: x == 'preto', cor)
        return self.resultado


class BuscaProfundidade(Buscas):
    def __init__(self):
        super().__init__()

    def search(self, data, estado_pai):
        cor = {}
        pred = {}
        d = {}
        f = {}

        tempo = 0

        for v in fn.list_state(estado_pai, []):
            cor[v] = 'branco'  # cores possíveis: branco cinza e preto
            pred[v] = None

        for v in fn.list_state(estado_pai, []):
            if cor[v] == 'branco':
                tempo = self.visit(estado_pai, v, cor, pred, d, f, tempo)

        self.resultado = filter(lambda x: x == 'preto', cor)
        return self.resultado

    def visit(self, G, s, cor, pred, d, f, tempo):
        tempo = tempo + 1
        d[s] = tempo
        cor[s] = 'cinza'

        for v in G.children:
            if cor[v] == 'branco':
                pred[v] = s
                tempo = self.visit(G, v, cor, pred, d, f, tempo)

        cor[s] = 'preto'
        tempo = tempo + 1
        f[s] = tempo

        return tempo
