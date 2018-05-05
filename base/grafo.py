from * import main.py

#Cria uma classe que vai representar um grafo.
class Graph_state:
    #Definindo uma função de inicialização do minha classe grafo. Entra () estão minhas 
    #variáveis que estão sendo criadas.
    def __init__(self, line, column, start=False):
        #Definindo minha váriavel "line=linha" da minha classe Graphe_state
        self.line = line
        #Definindo minha váriavel "column=coluna" da minha classe Graphe_state
        self.column = column
        #Definindo minha váriavel "start=startar" da minha classe Graphe_state
        self.start = start
        #Definindo minha váriavel "children=filho" da minha classe Graphe_state
        self.children = []
        #Definindo minha váriavel "parent=pai" da minha classe Graphe_state
        self.parent = None
        #Definindo minha váriavel "goal=objetivo" da minha classe Graphe_state
        self.goal = False

    #Definindo uma função para o meu objetivo 
    def isgoal(self, objective):
        #Se objetivo da minha linha for igual ao objetivo da linha do meu grafo e o objetivo 
        #da minha coluna for igual ao objetivo da coluna do meu grafo...
        if (objective[0] == self.line) and (objective[1] == self.column):
            #Quer dizer que o meu objetivo é verdadeiro.
            self.goal = True
    
    #Definindo função para adicionar meu objetivo no lugar de um filho na fila
    def add(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        repre = "(%d,%d)" % (self.line, self.column)
        return repre

#Cria uma classe aresta e define um objeto nos parametros para utilizar
class Aresta(object):
    #Definindo função de start com várieis criadas nos parâmetros.
    def __init__(self, g_ini=None, g_fim=None, custo=0):
        self.g_ini = g_ini
        self.g_fim = g_fim
        self.custo = custo

    def custoAresta(self):
        if (self.g_ini.column == self.g_fim.column):
            self.custo = self.g_fim.line - self.g_ini.line
            return self.custo
        else:
            self.custo = self.g_fim.column - self.g_ini.column
            return self.custo


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
