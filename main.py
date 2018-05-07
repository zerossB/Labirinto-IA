import time

import numpy as np
from PIL import Image

import base.funcoes as fn
from base.grafo import Graph_state
from base.buscas import BuscaLargura, BuscaProfundidade, BuscaCustoUniforme, BuscaGreedy, BuscaAEstrela

#Cria função main
def main():
    #Cria funçao de manipulação do tempo, desde o start da aplicação até o fim dela.
    t0 = time.time()

    #img_data = load_image('4 by 4 orthogonal maze.png')
    #Carrega a imagem passada na pasta do labirinto, com o nome da imagem "labirinto.png"
    img_data = fn.load_image('labirintos/labirinto.png')
    #img_data = load_image('100 by 100 orthogonal maze.png')

    #Armazena os valores do meu labirinto=img_data. Armazena em l_entrada o inicio do meu
    #labirinto em X=linha, armazena em c_entrada o inicio do meu labirinto em Y=coluna.
    l_entrada, c_entrada = fn.find_entry(img_data)
    #Armazena os valores de saída do meu labirinto=img_data. Armazena em lex o fim do meu 
    #labirinto na linha em X=linha, armazena em cex o fim do meu labirinto em Y=coluna.
    lex, cex = fn.find_exit(img_data)
    #Aqui está passando os valores da minha saída e definindo no meu objetivo.
    objective = (lex, cex)
    #Imprime na tela minha entrada.
    print("entrada: ", l_entrada, c_entrada)
    #Imprime na tela meu objetivo=saída.
    print("saida: ", objective, "\n")

    start_point = Graph_state(l_entrada, c_entrada, True)
    start_point.isgoal(objective)

    fn.find_next_intersection(img_data, start_point, fn.find_dir(
        img_data, l_entrada, c_entrada), objective)

    fn.count_custo(start_point, objective)

    print("Iniciando Busca em Largura")
    buscaLargura = BuscaLargura()
    t_ini = time.time()
    buscaLargura.search(img_data, start_point)
    t_fim = time.time()
    fn.printSpecs(t_ini, t_fim, buscaLargura)
    fn.drawLines(img_data, buscaLargura.visitado, "Largura")

    print("Iniciando Busca Profundidade")
    buscaProfundidade = BuscaProfundidade()
    t_ini = time.time()
    buscaProfundidade.search(img_data, start_point)
    t_fim = time.time()
    fn.printSpecs(t_ini, t_fim, buscaProfundidade)
    fn.drawLines(img_data, buscaLargura.visitado, "Profundidade")

    print("Iniciando Busca Custo Uniforme")
    buscaCustoUniforme = BuscaCustoUniforme()
    t_ini = time.time()
    buscaCustoUniforme.search(img_data, start_point)
    t_fim = time.time()
    fn.printSpecs(t_ini, t_fim, buscaCustoUniforme)
    fn.drawLines(img_data, buscaCustoUniforme.resultado, "Uniforme")

    print("Iniciando Busca Greedy")
    buscaGreedy = BuscaGreedy()
    t_ini = time.time()
    buscaGreedy.search(img_data, start_point)
    t_fim = time.time()
    fn.printSpecs(t_ini, t_fim, buscaGreedy)
    fn.drawLines(img_data, buscaGreedy.resultado, "Greedy")

    print("Iniciando Busca A*")
    buscaAEstrela = BuscaAEstrela()
    t_ini = time.time()
    buscaAEstrela.search(img_data, start_point)
    t_fim = time.time()
    fn.printSpecs(t_ini, t_fim, buscaAEstrela)
    fn.drawLines(img_data, buscaAEstrela.resultado, "A_Estrela")

if __name__ == '__main__':
    main()
