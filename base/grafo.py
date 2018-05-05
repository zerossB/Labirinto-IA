class Graph_state:
    def __init__(self, line, column, start=False):
        self.line = line
        self.column = column
        self.start = start
        self.children = []
        self.parent = None
        self.goal = False

    def isgoal(self, objective):
        if (objective[0] == self.line) and (objective[1] == self.column):
            self.goal = True

    def add(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        repre = "(%d,%d)" % (self.line, self.column)
        return repre


class Aresta(object):
    def __init__(self, g_ini=None, g_fim=None, custo=0):
        self.g_ini = g_ini
        self.g_fim = g_fim
        self.custo = custo

    def custoAresta(self):
        x = self.g_fim.line - self.g_ini.line
        y = self.g_fim.column - self.g_ini.column

        self.custo = x if x != 0 else y
        self.custo = self.custo if self.custo < 0 else self.custo * -1

        # if (self.g_ini.column == self.g_fim.column):
        #     self.custo = self.g_fim.line - self.g_ini.line
        #     return self.custo
        # else:
        #     self.custo = self.g_fim.column - self.g_ini.column
        #     return self.custo


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
