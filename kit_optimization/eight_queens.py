import random
random.seed()
TAM_TABULEIRO = 8

def select_elite(participantes, elite_tamanho):
  participantes.sort(key=evaluate)
  return participantes[0:elite_tamanho],participantes[elite_tamanho:]

def crossover(parent1,parent2, index):
  return [parent1[0:index]+parent2[index:], parent2[0:index]+parent1[index:]]


def mutate(individual,m,aggressive = False):
  if(m < 0.5 and aggressive):
    m += 0.2

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

def run_ga(g, n, k, m, e):
    populacao = cria_populacao(n)
    best = 99
    graph_data = ["Geracao | Best | Worst | Avg"]

    for gen in range(g):
      sum = 0
      for individuo in populacao:
        sum += evaluate(individuo)

      elite,populacao = select_elite(populacao,e)
      size_non_elite = len(populacao)

      current_best = evaluate(elite[0])
      current_worst = evaluate(populacao[-1])   
      current_avg = sum/n
      graph_data.append([gen,current_best,current_worst,current_avg])
      

      if(current_best < best):
        best = current_best
        print(f"{best=} || {elite[0]}")

        if(current_best == 0):
          print(f"Terminou em {gen=}")
          break

      #print(f"{len(elite)} selecionados, {len(populacao)} restantes")

      resultado_torneio = []
      while len(populacao) >= 2:
        participantes_torneio = []
        index1 = random.randint(0,len(populacao)-1)
        participantes_torneio.append(populacao.pop(index1))
        index2 = random.randint(0,len(populacao)-1)
        participantes_torneio.append(populacao.pop(index2))

        resultado_torneio.append ( tournament(participantes_torneio))


      #print(f"{len(resultado_torneio)} selecionados por torneio")
      resultado_torneio.sort(key=evaluate)
      nova_geracao = []
      pesos = [evaluated_weight(individuo) for individuo in resultado_torneio]
      

      while (len(nova_geracao) < size_non_elite):
        selected_parents = random.choices(resultado_torneio,weights = pesos,k=2)
        filhos = crossover(selected_parents[0],selected_parents[1],4)
        individuo1 = mutate(filhos[0],m, current_best == 1)
        individuo2 = mutate(filhos[1],m, current_best == 1)
        nova_geracao.extend([individuo1,individuo2])

      nova_geracao += elite  
      populacao = nova_geracao

      #print(f"{len(nova_geracao)} individuos para a próxima iteração")

      """
      Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
      :param g:int - numero de gerações
      :param n:int - numero de individuos
      :param k:int - numero de participantes do torneio
      :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
      :param e:int - número de indivíduos no elitismo
      :return:list - melhor individuo encontrado
      """


run_ga(1400,200,3,0.02,6)
