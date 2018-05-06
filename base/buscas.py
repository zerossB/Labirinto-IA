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

""" 
def busca_custo_uniforme(data, estado_pai, caminho_percorrido):
    global lista_peso
    global num_estado_visitado

    num_estado_visitado += 1

    if estado_pai.goal:
        data[estado_pai.line][estado_pai.column] = [255, 0, 0, 255]
        resultado.append(estado_pai)
    else:
        lista_caminho = []
        for peso_caminho in estado_pai.peso_aresta:
            del lista_caminho[:]
            if caminho_percorrido != None:
                lista_caminho.append(caminho_percorrido)
            lista_caminho.append(peso_caminho)
            lista_peso.append(list(lista_caminho))
        
        soma_peso_anterior = 0
        prox_estado = None
        melhor_caminho = None
        item_lista_peso_remove = None
        for item_lista_peso in lista_peso:
            soma_peso_atual = 0
            for item_lista_caminho in item_lista_peso:
                soma_peso_atual += item_lista_caminho.peso
                prox_estado_aux = item_lista_caminho.estado_destino
                melhor_caminho_aux = item_lista_caminho
                
            if soma_peso_atual < soma_peso_anterior or soma_peso_anterior == 0:
                soma_peso_anterior = soma_peso_atual
                prox_estado = prox_estado_aux
                melhor_caminho = melhor_caminho_aux
                item_lista_peso_remove = item_lista_peso

        lista_peso.remove(item_lista_peso_remove)

        busca_custo_uniforme(data, prox_estado, melhor_caminho)

        for estado_filho in estado_pai.children:
            if estado_filho in resultado:
                resultado.append(estado_pai)
"""


class BuscaCustoUniforme(Buscas):
    def __init__(self):
        super().__init__()
        self.cor = {}
    
    def search(self, estado_pai):
        filhos = estado_pai.arestas
        filhos = [filhos[x] for x in filhos]
        filhos = sorted(filhos, key=Aresta.get_custo)
        
        if not filhos:
            print("Não consegui encontrar o final :/")
        



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
        assert(len(data) == len(objetivo))  # each start time must match a finish time
        n = len(data)  # could be len f as well!
        a = []
        k = 0
        for m in range(1, n):
            if data[m] >= objetivo[k]:
                a.append(m)
                k = m
        return a