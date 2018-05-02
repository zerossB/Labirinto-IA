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
        self.cor = {}
        self.pred = {}
        self.d = {}

    def search(self, data, estado_pai):
        for v in fn.list_state(estado_pai, []):
            self.d[v] = np.inf
            self.cor[v] = 'branco'  # branco cinza e preto
            self.pred[v] = None

        self.cor[estado_pai] = 'cinza'
        self.d[estado_pai] = 0

        Q = Queue()
        Q.put(estado_pai)

        while not Q.empty():
            u = Q.get()

            if u.goal:
                break

            for v in u.children:
                if self.cor[v] == 'branco':
                    self.cor[v] = 'cinza'
                    self.d[v] = self.d[u] + 1
                    self.pred[v] = u

                    Q.put(v)
            self.cor[u] = 'preto'
            
        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']
        return self.resultado


class BuscaProfundidade(Buscas):
    def __init__(self):
        super().__init__()
        self.cor = {}
        self.pred = {}
        self.d = {}
        self.f = {}

    def search(self, data, estado_pai):
        tempo = 0

        for v in fn.list_state(estado_pai, []):
            self.cor[v] = 'branco'  # self.cores possíveis: branco cinza e preto
            self.pred[v] = None

        for v in fn.list_state(estado_pai, []):
            if self.cor[v] == 'branco':
                tempo = self.visit(estado_pai, v, self.cor, self.pred, self.d, self.f, tempo)

        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']
        return self.resultado

    def visit(self, G, s, cor, pred, d, f, tempo):
        tempo = tempo + 1
        d[s] = tempo
        self.cor[s] = 'cinza'

        for v in G.children:
            if self.cor[v] == 'branco':
                self.pred[v] = s
                tempo = self.visit(G, v, self.cor, self.pred, self.d, self.f, tempo)

        self.cor[s] = 'preto'
        self.tempo = tempo + 1
        self.f[s] = tempo

        return tempo
