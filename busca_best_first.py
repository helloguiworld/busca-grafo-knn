def criterio_ordenacao(item):
    return item[1]

def busca_best_first(grafo, inicio, fim):
    print("BUSCA BEST FIRST")

    vertices = grafo.get_vertices()

    fila = [[inicio, 0]]
    visitados = [inicio]
    historico = [[inicio, -1]]
    while fila:
        vertice_antecessor = fila[0][0]
        print("Fila:", fila)
        for aresta in vertices[vertice_antecessor].get_arestas():
            if aresta[0] not in visitados:
                fila.append([aresta[0], aresta[1]])
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
        