Mini Trabalho 3 – Exploração de Dados

Integrantes do Grupo
- Gabriel Guedes Fernandes - 232014656
- Artur Mendonça Arruda - 231033737
- João Marcelo Guimarães Costa Naves - 232014709
- Júlia Santana Campos - 232027494
- Davi Monteiro de Negreiros - 232013971

Descrição do projeto:
Este trabalho tem como objetivo realizar a análise exploratória do dataset "alzheimers_disease_data.csv", buscando identificar padrões, correlações e insights relevantes para orientar etapas futuras de modelagem de aprendizado de máquina.

Foram analisados diferentes grupos de variáveis, incluindo fatores clínicos, cognitivos, funcionais, comportamentais e demográficos. A partir dessas análises, foi possível compreender melhor a relação entre os atributos e o diagnóstico da doença de Alzheimer.

Estrutura dos arquivos:


=- notebooks
    - indicadores_clinicos.ipynb  
        Análise dos fatores clínicos, como doenças associadas e indicadores de saúde

    - capacidade_funcional.ipynb  
        Avaliação da capacidade funcional e impacto nas atividades diárias (ADL e FunctionalAssessment)

    - demografico.ipynb  
        Análise de variáveis populacionais, como idade, gênero e nível educacional

    - habitos_antecedentes.ipynb  
        Investigação de hábitos e histórico dos pacientes

    - sintese_correlacoes.ipynb  
        Consolidação das análises anteriores por meio da matriz de correlação global e identificação das variáveis mais relevantes para o diagnóstico
=- data
    - alzheimers_disease_data.csv
        Dataset utilizado.

Instruções para execução:

1. Instalar as dependências necessárias:
   - Python 3.x
   - pandas
   - matplotlib
   - seaborn

2. Garantir que o arquivos estejam nos diretórios descritos pela estrutura acima.

3. Executar os notebooks na seguinte ordem:
   - indicadores_clinicos.ipynb
   - capacidade_funcional.ipynb
   - demografico.ipynb
   - habitos_antecedentes.ipynb
   - sintese_correlacoes.ipynb