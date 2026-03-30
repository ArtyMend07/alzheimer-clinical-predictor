# Alzheimer Clinical Predictor

Este projeto é um trabalho acadêmico da disciplina de Aprendizado de Máquina na Universidade de Brasília. O objetivo é desenvolver uma ferramenta que ajude médicos de Unidades Básicas de Saúde a identificar precocemente sinais de Alzheimer, tentando diminuir o enorme abismo de subdiagnóstico que existe hoje no Brasil.

---

## 1. Integrantes do Grupo
* **Gabriel Guedes Fernandes** - 232014656
* **Artur Mendonça Arruda** - 231033737
* **João Marcelo Guimarães Costa Naves** - 232014709
* **Júlia Santana Campos** - 232027494
* **Davi Monteiro de Negreiros** - 232013971

---

## 2. Contexto do Projeto
O Alzheimer é um problema gigante de saúde pública, onde hoje, estima-se que 80% das pessoas com demência no Brasil sequer têm um diagnóstico oficial. Na prática, isso sobrecarrega os especialistas e atrasa o tratamento. Como o fluxo de atendimento no SUS é muito alto, a ideia é usar Machine Learning para analisar dados que o médico já coleta na rotina, como hábitos de vida e histórico de saúde, e gerar um alerta de risco automático.

Além de ajudar o paciente, isso tem um impacto financeiro direto. Prever a doença cedo ajuda o sistema a se planejar e pode reduzir custos que hoje chegam na casa dos bilhões para os cofres públicos e para as famílias.

---

## 3. Dados e Metodologia
Estamos trabalhando com o **Alzheimer's Disease Dataset** do Kaggle, que tem dados de cerca de 2 mil pacientes. O foco é cruzar os 14 fatores de risco listados pela *Lancet Commission* em 2024 com as avaliações que já são feitas na UBS.

**O que estamos analisando:**
* **Dados Clínicos:** Colesterol, pressão arterial e IMC.
* **Habilidades Diárias:** Atividades de vida diária (ADL) e o teste MMSE.
* **Estilo de Vida:** Qualidade de sono, dieta e exercícios.

Escolhemos o algoritmo **Random Forest** porque ele funciona muito bem com esse tipo de dado de tabela e, além disso, ele permite ver a importância das características. Assim, o médico consegue entender quais fatores pesaram mais no risco daquele paciente.

---

## 4. O que pretendemos validar
Nossas metas principais para esse semestre são:
1. Conseguir uma acurácia acima de **85%**.
2. Confirmar se a dificuldade em tarefas diárias (ADL) é mesmo o sinal mais forte de risco.
3. Testar se o controle do colesterol realmente faz diferença na predição para o grupo de 60 a 70 anos.

---

## Histórico de Versões
| Versão | Descrição | Autor(es) | Data | Revisor(es) | Data de Revisão |
|--------|-----------|-----------|------|-------------|-----------------|
| 1.0 | Criação da README do projeto, e inserção das informações iniciais. | [Artur Mendonça Arruda](https://github.com/ArtyMend07) | 30/03/2026 |  |  |