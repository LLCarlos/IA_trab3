import random
import matplotlib.pyplot as plt

random.seed()
TAM_TABULEIRO = 8

def select_elite(participantes, elite_tamanho):
  participantes.sort(key=evaluate)
  return participantes[0:elite_tamanho],participantes[elite_tamanho:]

def crossover(parent1,parent2, index):
  return [parent1[0:index]+parent2[index:], parent2[0:index]+parent1[index:]]


def mutate(individual,m,aggressive = False):
  if(m < 0.5 and aggressive):
    m += 0.5

  if(random.random() < m):
    index = random.randint(0,7)
    new_pos = random.randint(1,8)
    individual[index] = new_pos

  return individual


def tournament(participantes):
  best_participante = None
  best_aptitude = 99

  for index,participante in enumerate(participantes):
    current_aptitude = evaluate(participante)
    if(current_aptitude < best_aptitude):
      best_aptitude = current_aptitude
      best_participante = participante

  return best_participante



def evaluate (positions):
  attacks = 0


  for column,line in enumerate(positions):
    x1 = column
    y1 = line

    for column2,line2 in enumerate(positions[column+1:]):
      x2 = column + column2 + 1
      y2 = line2
      if(y1 == y2):
        attacks += 1

      elif(abs(y2-y1) == abs(x2-x1)):
        attacks += 1

  return attacks

def evaluated_weight(positions):
  resultado = evaluate(positions)
  return  10* (1/(1+resultado))


def cria_populacao(qtd):
  populacao = []

  for i in range(qtd):
    individuo = []
    for coluna in range(TAM_TABULEIRO):
      individuo.append( random.randint(1,8) )

    populacao.append(individuo)

  return populacao

def run_ga(g, n, k, m, e,debug = False):
    populacao = cria_populacao(n)
    best = 99
    worst = 0
    graph_data = [[],[],[],[]]

    for gen in range(g):
      sum = 0
      for individuo in populacao:
        sum += evaluate(individuo)

      elite,populacao = select_elite(populacao,e)
      size_non_elite = len(populacao)

      current_best = evaluate(elite[0])
      current_worst = evaluate(populacao[-1])   
      current_avg = sum/n
      graph_data[0].extend([gen])
      graph_data[1].extend([current_best])
      graph_data[2].extend([current_avg])
      graph_data[3].extend([current_worst])

      if(current_worst > worst):
        worst = current_worst
      

      if(current_best < best):
        best = current_best
        if(debug):
          print(f"{best=} || {elite[0]}")

        if(current_best == 0):
          if(debug):
            print(f"Terminou em {gen=}")
          break

      resultado_torneio = []

      
      while len(populacao) >= k:
        participantes_torneio = []
        for i in range(k):
          index = random.randint(0,len(populacao)-1)
          participantes_torneio.append(populacao.pop(index))

        resultado_torneio.append ( tournament(participantes_torneio))

      current_generation = resultado_torneio
      nova_geracao = []
      pesos = [evaluated_weight(individuo) for individuo in current_generation]

      

      while (len(nova_geracao) < n):
        selected_parents = random.choices(current_generation,weights = pesos,k=2)
        filhos = crossover(selected_parents[0],selected_parents[1],4)
        individuo1 = mutate(filhos[0],m, current_best == 1)
        individuo2 = mutate(filhos[1],m, current_best == 1)
        nova_geracao.extend([individuo1,individuo2])

      nova_geracao += elite  
      populacao = nova_geracao

    if(debug):
      plt.figure(figsize=(16, 16))
      plt.ylabel('Conflitos',fontsize = 16)
      plt.xlabel('Gerações',fontsize = 16)
      plt.plot(graph_data[0],graph_data[1],label='best')
      plt.plot(graph_data[0],graph_data[2],label='avg')
      plt.plot(graph_data[0],graph_data[3],label='worst')
      plt.yticks(range(worst+1))
      plt.grid();plt.legend();plt.show()
    
    return elite[0]

if __name__ == '__main__':
  print(run_ga(200,400,3,0.2,10,True))
