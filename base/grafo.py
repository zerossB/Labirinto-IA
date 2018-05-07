# Cria uma classe que vai representar um grafo.
class Graph_state:
    # Definindo uma função de inicialização do minha classe grafo. Entra () estão minhas
    # variáveis que estão sendo criadas.
    def __init__(self, line, column, start=False):
        # Definindo minha váriavel "line=linha" da minha classe Graphe_state
        self.line = line
        # Definindo minha váriavel "column=coluna" da minha classe Graphe_state
        self.column = column
        # Definindo minha váriavel "start=startar" da minha classe Graphe_state
        self.start = start
        # Definindo minha váriavel "children=filho" da minha classe Graphe_state
        self.children = []
        # Definindo minha váriavel "parent=pai" da minha classe Graphe_state
        self.parent = None
        # Definindo minha váriavel "goal=objetivo" da minha classe Graphe_state
        self.goal = False
        # Defino um Dicionário de arestas, utilizando o filho como Indice, consigo buscar o custo das arestas
        self.arestas = {}

    # Definindo uma função para o meu objetivo
    def isgoal(self, objective):
        # Se objetivo da minha linha for igual ao objetivo da linha do meu grafo e o objetivo
        # da minha coluna for igual ao objetivo da coluna do meu grafo...
        if (objective[0] == self.line) and (objective[1] == self.column):
            # Quer dizer que o meu objetivo é verdadeiro.
            self.goal = True

    # Definindo função para adicionar meu objetivo no lugar de um filho na fila
    def add(self, child):
        child.parent = self
        self.children.append(child)

    # A partir do Pai, calculo a distancia entre meus filhos
    def calcArestas(self, objective):
        for filho in self.children:
            aresta = Aresta(self, filho)
            aresta.custoAresta()
            aresta.custoHeuristica(objective)
            self.arestas[filho] = aresta

    def __str__(self):
        repre = "(%d,%d)" % (self.column, self.line)
        return repre

    def __lt__(self, other):
        return ((self.line, self.column) <
                (other.line, other.column))


# Cria uma classe aresta e define um objeto nos parametros para utilizar
class Aresta(object):
    # Definindo função de start com várieis criadas nos parâmetros.
    def __init__(self, g_ini=None, g_fim=None, custo=0, custoH=0):
        self.g_ini = g_ini
        self.g_fim = g_fim
        self.custo = custo
        self.custoH = custoH

    def get_custo(self):
        return self.custo

    def get_heuristica(self):
        return self.custoH

    # Faço o custo da minha Aresta/Vertice
    def custoAresta(self):
        x = self.g_fim.column - self.g_ini.column
        y = self.g_fim.line - self.g_ini.line

        self.custo = x if x != 0 else y
        if self.custo < 0:
            self.custo = self.custo * -1
        self.custo = self.custo + 2

    def custoHeuristica(self, objetivo):
        oX, oY = objetivo[0], objetivo[1]
        gX, gY = self.g_ini.column, self.g_ini.line

        self.custoH = (oX - gX) + (oY - gY)
        if self.custoH < 0:
            self.custoH = self.custoH * -1

    def __str__(self):
        return str(self.g_ini) + " " + str(self.g_fim) + " " + str(self.custo) + " " + str(self.custoH)


# def busca_largura(data, estado_pai):
#     visitado = list()
#     marcado = list()
#     resultado = list()

#     visitado.append(estado_pai)

#     if estado_pai in marcado:
#         marcado.remove(estado_pai)
#     print("Visitado: %s" % str(estado_pai))

#     for estado_filho in estado_pai.children:
#         if not estado_filho in marcado and not estado_filho in visitado:
#             marcado.append(estado_filho)
#             print("Marcado: %s" % str(estado_filho))

#     for estado_filho in marcado:
#         busca_largura(data, estado_filho)

#     if estado_pai.goal:
#         data[estado_pai.line][estado_pai.column] = [255, 0, 0, 255]
#         resultado.append(estado_pai)

#     for estado_filho in estado_pai.children:
#         if estado_filho in resultado:
#             data[estado_pai.line][estado_pai.column] = [255, 0, 0, 255]
#             resultado.append(estado_pai)
