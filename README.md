# ClusterClientes

## Descrição do projeto e definição do problema de negócio
Projeto dedicado à análise de perfil de clientes de uma empresa, a qual desejava dividir estes em 3 categorias para melhor orientar suas campanhas, porém sem ter um critério bem definido. Com a definição do objetivo de encntrar 3 clusters para os clientes foi definida a utilização do algoritmo k-means e foi realizado o tratamento e preparação dos dados já com foco no modelo a ser utilizado numa primeira tentativa.
(código python e dashboard do power bi estão disponíveis no repositório, assim como dados de entrada e saída do modelo em csv)

## Passo a passo
## Análise 
A parte de análise exploratória e preparação dos dados foi feita através do carregamento do arquivo csv disponibilizado onde continha as seguintes informações dos clientes:
    * ID
    * Idade
    * Renda Anual
    * Pontuação de gastos

## Preparação dos dados
A partir da primeira análise nas variáveis de interesse via resumo estatístico, inicia-se a preparação dos dados para o algoritmo de machine learning k-means, que assim como a maioria dos modelos, espera receber as entradas na mesma escala. O que neste caso, não acontece pela própria natureza das variáveis (exemplo: idade e renda anual).

## Treinamento do modelo e resultados
Portanto, os dados foram convertidos através da escala logarítmica e entregues ao modelo para treinamento.
Por fim, o resultado da segmentação de cada cliente foi incorporada a uma nova coluna do dataframe e exportado como um novo arquivo csv. Esse arquivo agora serviu como base para a criação do dashboard onde foram representadas as características de cada grupo.

## Conclusão e insights
![image](https://github.com/augustorvasques/ClusterClientes/assets/166548437/7000ce74-0323-4c1e-9fed-97f40eb7005f)

Como conclusão, podemos observar através do dashboard que a quantidade de clientes em cada grupo é semelhante, e analisando o gráfico de média de idade de cada cluster pode-se observar que houve pouca diferença entre eles e, portanto, provavelmente não foi uma variável importante na segmentação realizada pelo modelo. Já no gráfico que mostra a média de pontuação de gastos e de renda anual de cada cluster, podemos ver grandes diferenças e ter uma ideia dos critérios de divisão adotado pelo k-means.

O primeiro grupo apresenta pontuação de gastos alta enquanto possui renda média baixa. Já o segundo também possui renda média baixa mas é acompanhado por uma pontuação de gastos baixa. O terceiro, difere dos demais por possuir uma renda média alta (poder de compra) enquanto a pontuação de gastos não acompanha essa proporção, ou seja, não é tão alta quanto por exemplo do grupo 1, que possui a menor média de renda. Possivelmente, este grupo de clientes possui maior margem de crescimento nas vendas, já que sua relação gastos/renda é bem inferior aos outros 2.

Dessa forma, a área de marketing pode conhecer melhor seus clientes e realizar campanhas direcionadas e mais efetivas.
