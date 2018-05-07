#'Importa pacote Numpy e renomeia com NP'
import numpy as np
#'Importa módulo base.funcoes e renomeia para FN'
import base.funcoes as fn

from base.grafo import Aresta

#'De Pillow importar Image, ImageDraw'
from PIL import Image, ImageDraw
#'De queue=fila importar Queue, LifoQueue'
from queue import Queue, LifoQueue
#'De base.funcoes importar addQueue'
from base.funcoes import addQueue

#'Criando classe chamada Buscas(parâmetro{object}):'


class Buscas(object):
    #'Definindo função de inicialização para a classe buscas=self'
    def __init__(self):
        #'buscas=self aponta para visitado que é um array vazio'
        self.visitado = []
        #'self aponta para marcado que é um array vazio'
        self.marcado = []
        #'self aponta para resultado que é um arrayvazio'
        self.resultado = []

    def drawPoint(self, data, aresta, color):
        if color == 'branco':
            data[aresta.line][aresta.column] = [255, 255, 255, 255]
        elif color == 'cinza':
            data[aresta.line][aresta.column] = [0, 0, 135, 255]
        else:
            data[aresta.line][aresta.column] = [255, 69, 0, 255]


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


class BuscaCustoUniforme(Buscas):
    """
    Algoritmo Busca - Uniforme
    1. Definir um conjunto L de nós iniciais

    2. Ordene L em ordem crescente de custo

    3. Se L é vazio
        Então Busca não foi bem sucedida
        Senão seja n o primeiro nó de L;

    4. Se n é um nó objetivo
        Então
            Retornar caminho do nó inicial até N;
            Parar
        Senão
            Remover n de L;
            Adicionar em L todos os nós filhos de n, rotulando cada nó com o seu caminho até o nó inicial;
            Ordene L em ordem crescente de custo;
            Volte ao passo 3.
    """

    def __init__(self):
        super().__init__()
        self.cor = {}

    def search(self, estado_pai):
        filhos = estado_pai.arestas
        filhos = [filhos[x] for x in filhos]
        filhos = sorted(filhos, key=Aresta.get_custo)

        for v in filhos:
            # cores possíveis: branco, cinza e preto
            self.cor[v] = 'branco'
        
        if not filhos:
            print("Lista Vazia")

        filho = filhos[-1]
        print(filho)

        if filho.g_ini.goal:
            print("Objetivo chego")
            return
        else:
            self.search(filho.g_fim)


class BuscaGreedy(Buscas):
    def __init__(self):
        super().__init__()

    def search(self, data, objetivo):
        """
            Args:
                s: a list of start times
                f: a list of finish times
            Returns:
                A maximal set of activities that can be scheduled.
                (We use a list to hold the set.)
        """
        assert(len(data) == len(objetivo)
               )  # each start time must match a finish time
        n = len(data)  # could be len f as well!
        a = []
        k = 0
        for m in range(1, n):
            if data[m] >= objetivo[k]:
                a.append(m)
                k = m
        return a
