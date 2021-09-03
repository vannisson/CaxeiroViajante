from itertools import permutations

def GerarCaminhos(cidades):
    Nodes = [node for node in range(len(cidades))]
    Node = Nodes.pop()
    nodePermutations = list(permutations(Nodes))
    Tree = list(map(list, nodePermutations))
    for paths in Tree:
        paths.append(Node)
        paths.append(paths[0])  
    return Nodes, Tree

def BruteForce(cidades):
    Nodes, Trees = GerarCaminhos(cidades)
    costList = []
    for ciclo in Trees:
        costPerCicle = 0
        for index in range(0,(len(Nodes)-1)):
            costPerCicle = costPerCicle + cidades[ciclo[index]][ciclo[index+1]]
        costList.append(costPerCicle)
    lastCost = min(costList)
    lastCostIndex = costList.index(lastCost)
 
    return [lastCost,trees]
