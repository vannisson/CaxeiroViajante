import sys
#? sys em Python fornece várias funções e variáveis ​​que são usadas para 
#? manipular diferentes partes do ambiente de execução Python

def vizinhoProximoPCV(matrizAdj, inicio):
  #! Escolhe um vértice inicial
  atual = inicio
  #! Define uma variável para definir o próximo vértice a ser acessado
  proximo = 0
  #! Calcula a distância entre o vértice atual e o próximo
  #? sys.maxsize indica o maior valor endereçável que esta implementação do Python
  distancia_proximo = sys.maxsize
  #! Define uma variável para definir o tamanho do caminho percorrido
  tamanho_caminho = 0
  #! Define uma variável que vai armazenar os vértices já visitados
  visitados = []
  #! Define uma variável que vai armazenar as distâncias dos vértices
  distancias = []
  #! Cria uma variável auxiliar para acessar o vértice de índice 0 na matriz de adjacência
  zero = len(matrizAdj[0])

  #* Começa um loop para percorrer todos os vértices próximos
  while tamanho_caminho < zero-1:

    for valor in range(zero):

      if (atual != valor and valor not in visitados):
        #! Checa qual caminho para os vértices adjacentes tem o menor custo
        if (distancia_proximo > float(matrizAdj[atual][valor])):
          distancia_proximo = float(matrizAdj[atual][valor])
          proximo = valor

    #! Salva o vértice atual nos visitados
    visitados.append(atual)
    #! Passa para o próximo vértice
    atual = proximo
    
    #* Se todos os vértices já forem visitados ele para o loop
    if tamanho_caminho == zero:
      break
    
    #* Se não, ele continua no loop e passa para o próximo vértice
    else:
      distancias.append(distancia_proximo)
      distancia_proximo = sys.maxsize
      tamanho_caminho += 1
  
  #! Pega a distância total, através do primeiro vértice visitado e do último(salvo na último loop em "proximo")
  distancia_maxima = float(matrizAdj[visitados[0]][proximo])
  #! Salva os vértices visitados
  visitados.append(visitados[0])
  visitados.append(proximo)
  #! Salva a distância
  distancias.append(distancia_maxima)
  #! Soma todos os elementos da matriz, pegando uma distância total
  distancia_total = sum(distancias)

  print("Menor custo obtido:",distancia_total)

  print("Vértices visitados:",visitados)