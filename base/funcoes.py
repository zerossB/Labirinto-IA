import numpy as np
import sys

from PIL import Image, ImageDraw

from base.grafo import Graph_state


def addQueue(path, pixel):
    novo_path = list(path)
    novo_path.append(pixel)
    return novo_path

# Função para gerar uma solução


def geraResolucao(path, name, full_path=[], show=False):
    """
        Pego a minha solução e coloco a linha vermelha
            no caminho correto
    """
    # Carrega meu labirinto e atribui o valor dele em "data"
    data = load_image("labirintos/labirinto.png")

    #
    for posicao in full_path:
        data[posicao.line][posicao.column] = [255, 0, 255, 255]

    # for posicao in path:
    #     data[posicao.line][posicao.column] = [255, 0, 0, 255]

    name_file = "Resolucao-"+name+".png"
    save_image(data, "resolv/"+name_file)


def printSpecs(t_ini, t_fim, busca, path, count, full_path):
    """
        Printa informações sobre as funções
    """
    print("\nTempo de Resolução: ", t_fim - t_ini, "ms")
    print("Metodo de Busca: ", busca)
    print("Número de estados Analisados ", count)
    print("Número de estados p/ Solução: ", len(path))
    print("Memória Alocada: ", sys.getsizeof(path), "KBytes")
    print("Memória Total Alocada: ", sys.getsizeof(full_path), "KBytes")


def load_image(infilename):
    """
    Carrego minha imagem e a transformo em uma matriz de 32bits
    """
    img = Image.open(infilename)
    # impixels = img.load()
    # img.show()
    # print(impixels[0,0])
    print(img.getbands())
    data = np.asarray(img, dtype="int32")
    print("Image shape: ", data.shape)
    return data


def drawLines(data, visitados, filename):
    img = Image.fromarray(np.asarray(
        np.clip(data, 0, 255), dtype="uint8"), "RGBA")
    draw = ImageDraw.Draw(img)
    
    for g_ini, g_fim in visitados:
        draw.line(
            (g_ini.column, g_ini.line,
                g_fim.column, g_fim.line),
            fill=(255, 0, 0), width=2
        )

    # draw.line(lines, fill=255, width=2)
    # draw.line((0, img.size[1], img.size[0], 0), fill=128, width=2)

    name_file = "Resolucao-Lines-"+filename+".png"
    img.save("resolv/"+name_file)


def save_image(npdata, outfilename):
    """
        Pego minha matriz de pixels, e tranformo em uma imagem.
    """
    print("Saved image shape: ", npdata.shape)
    #img = Image.fromarray(npdata,"RGBA")
    img = Image.fromarray(np.asarray(
        np.clip(npdata, 0, 255), dtype="uint8"), "RGBA")
    img.save("resolv/" + outfilename)

# Cria função para entrada do labirinto


def find_entry(data):
    """
        Procuro o inicio do meu labirinto
    """
    # for i in data[0]:
    # print data[0].shape
    #
    for index, x in enumerate(data[0]):
        # Se o array de X que é 0 for igual a
        if x[0] == 0:
            # print(index)
            # print(data[2][index][0])
            # Retornar meu ..... e meu index.
            return 0, index

# Cria uma função de saída


def find_exit(data):
    """
        Procuro a saida do meu labirinto
    """
    wd, hd, sd = data.shape
    for index, x in enumerate(data[-1]):
        if x[0] == 0:
            return wd-2, index


def count_state(root_state, count):
    for s in root_state.children:
        count += 1
        count += count_state(s, 0)
    return count


def count_custo(root_state):
    root_state.calcArestas()
    for filho in root_state.children:
        count_custo(filho)


def list_state(root_state, lista):
    for s in root_state.children:
        lista.append(s)
        list_state(s, lista)
    return lista


def print_states(root_state, output):
    if root_state.start:
        output += "R:"+str(root_state) + ";"
    elif root_state.goal:
        output += "**"+str(root_state) + "**;"
    else:
        output += str(root_state) + ";"
    for s in root_state.children:
        output += print_states(s, "")
    return output


def draw_path(data, root_state):
    if root_state.start:
        data[root_state.line][root_state.column] = [0, 255, 0, 255]
    elif root_state.goal:
        data[root_state.line][root_state.column] = [255, 0, 0, 255]
    else:
        data[root_state.line][root_state.column] = [255, 255, 0, 255]
    for s in root_state.children:
        draw_path(data, s)


def colorir_caminho(data, act_state, objective):
    wd, hd, sd = data.shape

    if act_state.column == objective.column:
        distancia_estado = objective.line - act_state.line
        if distancia_estado < 0:
            for x in range(abs(distancia_estado)):
                data[act_state.line - x][act_state.column] = [255, 0, 0, 255]
        else:
            for x in range(distancia_estado):
                data[x + act_state.line][act_state.column] = [255, 0, 0, 255]
    elif act_state.line == objective.line:
        distancia_estado = objective.column - act_state.column
        if distancia_estado < 0:
            for y in range(abs(distancia_estado)):
                data[act_state.line][act_state.column - y] = [255, 0, 0, 255]
        else:
            for y in range(distancia_estado):
                data[act_state.line][y + act_state.column] = [255, 0, 0, 255]


def marcar_caminho(data, estado_pai, resultado):
    estado_inicio = estado_pai
    for estado in reversed(resultado):
        if estado == estado_pai:
            continue
        estado_final = estado
        colorir_caminho(data, estado_inicio, estado_final)
        estado_inicio = estado_final


def find_dir(data, l, c, block=2):
    right = 0
    left = 0
    top = 0
    down = 0
    wd, hd, sd = data.shape
    # right
    if c < wd-block and data[l][c+block][0] == 0:
        right = block
    # left
    if c > block and (data[l][c-block][0] == 0 or data[l+1][c-block][0] == 0):
        left = block
    # down
    if l < hd-block and data[l+block][c][0] == 0:
        down = block
    # top
    if l > block and (data[l-block][c][0] == 0 or data[l-block][c+1][0] == 0):
        top = block
    return right, down, left, top


def find_next_intersection(data, act_state, vector, objective):
    wd, hd, sd = data.shape
    if vector[0] != 0:
        # go right
        for x in range(act_state.column+vector[0], wd, vector[0]):
            right, down, left, top = find_dir(data, act_state.line, x)

            if right == 0:  # found an edge
                new_state = Graph_state(act_state.line, x)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection right at: ",act_state.line,x)
                #print(" -> can go: ",(0,down,0,top))
                find_next_intersection(
                    data, new_state, (0, down, 0, top), objective)
                break
            if down != 0 or top != 0:
                new_state = Graph_state(act_state.line, x)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection right at: ",act_state.line,x)
                #print(" -> can go: ",(0,down,0,top))
                find_next_intersection(
                    data, new_state, (0, down, 0, top), objective)
    if vector[1] != 0:
        # go down
        for y in range(act_state.line+vector[1], hd, vector[1]):
            right, down, left, top = find_dir(data, y, act_state.column)
            if down == 0:  # found an edge
                new_state = Graph_state(y, act_state.column)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection down at: ",y,act_state.column)
                #print(" -> can go: ",(right,0,left,0))
                find_next_intersection(
                    data, new_state, (right, 0, left, 0), objective)
                break
            if right != 0 or left != 0:
                new_state = Graph_state(y, act_state.column)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection down at: %d,%d -> can go: %r"%(y,act_state.column,(right,0,left,0)))
                find_next_intersection(
                    data, new_state, (right, 0, left, 0), objective)
    if vector[2] != 0:
        # go left
        for x in range(act_state.column-vector[2], 0, -vector[2]):
            right, down, left, top = find_dir(data, act_state.line, x)
            if left == 0:  # found an edge
                new_state = Graph_state(act_state.line, x)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection left at: ",act_state.line,x)
                #print(" -> can go: ",(0,down,0,top))
                find_next_intersection(
                    data, new_state, (0, down, 0, top), objective)
                break
            if down != 0 or top != 0:
                new_state = Graph_state(act_state.line, x)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection left at: %d,%d  -> can go: %r"%(act_state.line,x,(0,down,0,top)))
                find_next_intersection(
                    data, new_state, (0, down, 0, top), objective)
    if vector[3] != 0:
        # go up
        for y in range(act_state.line-vector[3], 0, -vector[3]):
            right, down, left, top = find_dir(data, y, act_state.column)
            if top == 0:  # found an edge
                new_state = Graph_state(y, act_state.column)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection up at: ",y,act_state.column)
                #print(" -> can go: ",(right,0,left,0))
                find_next_intersection(
                    data, new_state, (right, 0, left, 0), objective)
                break
            if right != 0 or left != 0:
                new_state = Graph_state(y, act_state.column)
                new_state.isgoal(objective)
                act_state.add(new_state)
                #print("intersection up at: %d,%d -> can go: %r"%(y,act_state.column,(right,0,left,0)))
                find_next_intersection(
                    data, new_state, (right, 0, left, 0), objective)
