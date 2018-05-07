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

    # Está atribuindo os valores para de inicio com base nos valores capturados de X e Y para
    # a variavel Start_point sendo Lex como x e Cex como y
    start_point = Graph_state(l_entrada, c_entrada, True)


    # Verifica se meu ponto inicial ja é o meu objetivo
    start_point.isgoal(objective)

    # Encontra a proxima intersecção possivel e descobre se irá ir pra direita,
    # esquerda pra baixo ou pra cima verificando aonde tem caminho possivel
    fn.find_next_intersection(img_data, start_point, fn.find_dir(
        img_data, l_entrada, c_entrada), objective)

    # Descobre o "custo" da distancia entre o ponto inicial e o objetivo
    fn.count_custo(start_point, objective)


    #COMECO DA BUSCA EM LARGURA


    print("Iniciando Busca em Largura")
    buscaLargura = BuscaLargura()
    # Pega o tempo inicial da busca
    t_ini = time.time()
    # Executa toda a busca em largura
    buscaLargura.search(img_data, start_point)
    # Pega o tempo do fim da execução da busca
    t_fim = time.time()
    # Printa o tempo levado na busca, o nome da busca, quantos estados foram
    # analizados, o numero de estados necessarios pra resulução final e a 
    # memoria que foi alocada
    fn.printSpecs(t_ini, t_fim, buscaLargura)
    # Gera a imagem e pinta os estados visitados durante a busca
    fn.drawLines(img_data, buscaLargura.visitado, "Largura")


    # COMECO DA BUSCA EM PROFUNDIDADE


    print("Iniciando Busca Profundidade")
    buscaProfundidade = BuscaProfundidade()
    # Pega o tempo inicial da busca
    t_ini = time.time()
    # Executa toda a busca em Profundidade
    buscaProfundidade.search(img_data, start_point)
    # Pega o tempo do fim da execução da busca
    t_fim = time.time()
    # Printa o tempo levado na busca, o nome da busca, quantos estados foram
    # analizados, o numero de estados necessarios pra resulução final e a 
    # memoria que foi alocada
    fn.printSpecs(t_ini, t_fim, buscaProfundidade)
    # Gera a imagem e pinta os estados visitados durante a busca
    fn.drawLines(img_data, buscaLargura.visitado, "Profundidade")


    # COMECO DA BUSCA COM CUSTO UNIFORME


    print("Iniciando Busca Custo Uniforme")
    buscaCustoUniforme = BuscaCustoUniforme()
    # Pega o tempo inicial da busca   
    t_ini = time.time()
    # Executa toda a busca de Custo uniforme
    buscaCustoUniforme.search(img_data, start_point)
    # Pega o tempo do fim da execução da busca
    t_fim = time.time()
    # Printa o tempo levado na busca, o nome da busca, quantos estados foram
    # analizados, o numero de estados necessarios pra resulução final e a 
    # memoria que foi alocada
    fn.printSpecs(t_ini, t_fim, buscaCustoUniforme)
    # 
    fn.drawLines(img_data, buscaCustoUniforme.resultado, "Uniforme")


    # COMECO DA BUSCA GREEDY


    print("Iniciando Busca Greedy")
    buscaGreedy = BuscaGreedy()
    # Pega o tempo inicial da busca
    t_ini = time.time()
    # Executa toda a busca Greedy
    buscaGreedy.search(img_data, start_point)
    # Pega o tempo do fim da execução da busca
    t_fim = time.time()
    # Printa o tempo levado na busca, o nome da busca, quantos estados foram
    # analizados, o numero de estados necessarios pra resulução final e a 
    # memoria que foi alocada    
    fn.printSpecs(t_ini, t_fim, buscaGreedy)
    # 
    fn.drawLines(img_data, buscaGreedy.resultado, "Greedy")


    # COMECO DA BUSCA A*


    print("Iniciando Busca A*")
    buscaAEstrela = BuscaAEstrela()
    # Pega o tempo inicial da busca
    t_ini = time.time()
    # Executa toda a busca A*
    buscaAEstrela.search(img_data, start_point)
    # Pega o tempo do fim da execução da busca
    t_fim = time.time()
    # Printa o tempo levado na busca, o nome da busca, quantos estados foram
    # analizados, o numero de estados necessarios pra resulução final e a 
    # memoria que foi alocada
    fn.printSpecs(t_ini, t_fim, buscaAEstrela)
    #
    fn.drawLines(img_data, buscaAEstrela.resultado, "A_Estrela")

if __name__ == '__main__':
    main()
