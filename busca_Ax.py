from graph_knn import distancia_euclidiana

def criterio_ordenacao(item):
    return item[1]

def busca_Ax(grafo, inicio, fim):
    """Busca A* usando como h(n) a distância euclidiana."""
    print("BUSCA A")

    vertices = grafo.get_vertices()

    fila = [[inicio, 0]]
    visitados = [inicio]
    historico = [[inicio, -1]]
    while fila:
        vertice_antecessor = fila[0][0]
        print("Fila:", fila)
        for aresta in vertices[vertice_antecessor].get_arestas():
            if aresta[0] not in visitados:
                distancia = distancia_euclidiana(vertices[aresta[0]].get_coordenadas(), vertices[fim].get_coordenadas())
                fila.append([aresta[0], aresta[1] + distancia])
                visitados.append(aresta[0])
                historico.append([aresta[0], vertice_antecessor])

        fila.pop(0)
        fila.sort(key=criterio_ordenacao)
    
    print()
    print("Visitados:", visitados)
    print("Histórico:", historico)

    caminho = []
    if fim not in visitados:
        print(f"Não possui caminho de {inicio} até {fim}. :(")
    else:
        print("Tem caminho!")
        vertice = fim
        while vertice != inicio:
            caminho.append(vertice)
            vertice = historico[visitados.index(vertice)][1]

        caminho.append(vertice)
        print(caminho)

    print()
    return caminho
        