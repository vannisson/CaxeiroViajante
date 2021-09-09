from sys import maxsize
from itertools import permutations

def PCVbruteforce(grafo,inicio):
    # Salvando os vértices
    vertices = []
    for vert in range(len(grafo)):
        if vert != inicio:
            vertices.append(vert)

    prox = permutations(vertices)
    caminhoAtual = maxsize
    
    # Fazendo o cálculo de custo
    for vert in prox:
        custoAtual = 0
        x = inicio
        for aresta in vert:
            custoAtual+=float(grafo[x][aresta])
            x = aresta
        custoAtual += float(grafo[x][inicio])
        caminhoMin = min(caminhoAtual,custoAtual)
        
        if caminhoMin < caminhoAtual:
            caminhoAtual = min(caminhoAtual,custoAtual)
            aux = vert

    # Decidindo o melhor caminho
    melhorCaminho = []
    for vert in aux:
        melhorCaminho.append(vert)

    melhorCaminho.insert(0, inicio)
    melhorCaminho.append(inicio)

    return [caminhoAtual,melhorCaminho]
