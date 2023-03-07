Bibliotecas adicionais:
random
matplotlib

1. Genética da realeza

1.1 Parâmetros utilizados:
  g = 200, n = 400, k = 3, m = 0.2, e = 10

1.2 Modificações

Uma modificação feita no algoritmo genético utilizado nesse código em comparação com o original, é o uso de uma taxa de mutação adaptativa. Quando a execução do 
programa chega em 1 conflito para pelo menos 1 indivíduo, e a taxa de mutação atual é inferior a 0.5, aumenta-se essa taxa por 0.5 com o intuíto de aumentar
as chances de que um indivíduo com 1 conflito sofra a mutação necessária para que ele chegue em 0 conflitos.
Em uma cursória experimentação de algumas dezenas de execuções, percebeu-se uma aparente melhora no sucesso do programa. Não só a maioria das execuções chegam na 
solução ótima em menos de 20 gerações, mas como os piores casos não passam de 200 com exceções extremamente raras.

2. Algoritmo de gradiente descendente / descida de gradiente para regressão linear.

- alpha: 0.001
- theta_0: -1
- theta_1: 1
- num_iterations: 10000
- MSE: 8.52854301222427