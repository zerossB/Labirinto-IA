#'Importa pacote Numpy e renomeia com NP'
import numpy as np
#'Importa módulo base.funcoes e renomeia para FN'
import base.funcoes as fn

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

    #'Definindo função desenha imagem(chamando o parâmetro{classe buscas}{data})'
    def drawImage(self, data):
        #
        img = Image.fromarray(np.asarray(
            np.clip(data, 0, 255), dtype="uint8"), "RGBA")
        #'Renderiza a imagem'
        draw = ImageDraw.Draw(img)

        #'Para uma chave no intervalo(parâmetro)'
        for key in range(1, len(self.resultado)):
            #'Passar'
            pass

        #'Nome do arquivo'
        name_file = "Resolucao.png"
        #'img aponta para salvar()'
        img.save("resolv/"+name_file)


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
            # cores possíveis: branco, cinza e preto
            self.cor[v] = 'branco'
            self.pred[v] = None

        for v in fn.list_state(estado_pai, []):
            if self.cor[v] == 'branco':
                tempo = self.visit(estado_pai, v, tempo)

        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']
        return self.resultado

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
