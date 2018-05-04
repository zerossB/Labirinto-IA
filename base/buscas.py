import numpy as np
import base.funcoes as fn

from PIL import Image, ImageDraw
from queue import Queue, LifoQueue
from base.funcoes import addQueue


class Buscas(object):
    def __init__(self):
        self.visitado = []
        self.marcado = []
        self.resultado = []

    def drawPoint(self, data, aresta, color):
        if color == 'branco':
            data[aresta.line][aresta.column] = [255, 255, 0, 255]
        elif color == 'cinza':
            data[aresta.line][aresta.column] = [255, 0, 255, 255]
        else:
            data[aresta.line][aresta.column] = [255, 255, 255, 255]


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
            self.drawPoint(data, v, self.cor[v])

        self.cor[estado_pai] = 'cinza'
        self.d[estado_pai] = 0
        self.drawPoint(data, estado_pai, self.cor[estado_pai])

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
                    self.drawPoint(data, v, self.cor[v])

                    Q.put(v)
            self.cor[u] = 'preto'
            self.drawPoint(data, u, self.cor[u])

        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']
        fn.save_image(data, "Resolucao-Largura.png")


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
            # cores possíveis: branco, cinza e preto
            self.cor[v] = 'branco'
            self.pred[v] = None

        for v in fn.list_state(estado_pai, []):
            if self.cor[v] == 'branco':
                tempo = self.visit(estado_pai, v, tempo)

        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']

    def visit(self, G, s, tempo):
        tempo = tempo + 1
        self.d[s] = tempo
        self.cor[s] = 'cinza'

        for v in G.children:
            if self.cor[v] == 'branco':
                self.pred[v] = s
                tempo = self.visit(G, v, tempo)

        self.cor[s] = 'preto'
        self.tempo = tempo + 1
        self.f[s] = tempo

        return tempo
