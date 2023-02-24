import random
random.seed()

def select_elite(participantes, elite_tamanho):
  participantes.sort(key=evaluate)
  return participantes[0:elite_tamanho]

def crossover(parent1,parent2, index):
  return [parent1[0:index]+parent2[index:], parent2[0:index]+parent1[index:]]


def mutate(individual,m):
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

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    raise NotImplementedError  # substituir pelo seu codigo
