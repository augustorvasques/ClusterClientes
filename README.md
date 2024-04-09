# ClusterClientes

## Descrição do projeto
Projeto dedicado à análise de perfil de clientes de uma empresa, a qual desejava dividir estes em 3 categorias para melhor orientar suas campanhas, porém sem ter um critério bem definido. Com a definição do objetivo de encntrar 3 clusters para os clientes foi definida a utilização do algoritmo k-means e foi realizado o tratamento e preparação dos dados já com foco no modelo a ser utilizado numa primeira tentativa.

## Passo a passo
A parte de análise exploratória e preparação dos dados foi feita através do carregamento do arquivo csv disponibilizado onde continha as seguintes informações dos clientes:
    * ID
    * Idade
    * Renda Anual
    * Pontuação de gastos
A partir da primeira análise nas variáveis de interesse via resumo estatístico, inicia-se a preparação dos dados para o algoritmo de machine learning k-means, que assim como a maioria dos modelos, espera receber as entradas na mesma escala. O que neste caso, não acontece pela própria natureza das variáveis (exemplo: idade e renda anual).
Portanto, os dados foram convertidos através da escala logarítmica
