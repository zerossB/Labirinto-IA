from base.graph import Grafo

if __name__ == '__main__':

    g = Grafo()

    g.add_vertice('a')
    g.add_vertice('b')
    g.add_vertice('c')
    g.add_vertice('d')
    g.add_vertice('e')
    g.add_vertice('f')

    g.add_aresta('a', 'b', 7)
    g.add_aresta('a', 'c', 9)
    g.add_aresta('a', 'f', 14)
    g.add_aresta('b', 'c', 10)
    g.add_aresta('b', 'd', 15)
    g.add_aresta('c', 'd', 11)
    g.add_aresta('c', 'f', 2)
    g.add_aresta('d', 'e', 6)
    g.add_aresta('e', 'f', 9)

    for v in g:
        for w in v.get_conexoes():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_custo(w)))
    
    print('')

    for v in g:
        print('g.vert_dict[%s] = %s' % (v.get_id(), g.vertices[v.get_id()]))
