# Projeto Final MLE
## Configuração do ambiente
Para configurar o ambiente no terminal projeto siga as intruções abaixo:
- 1: Criar um ambiente virtual com python 3.11 : 
```
python3.11 -m venv .venv
```
- 2: Ative o ambiente :
```
source .venv/bin/activate # macOS / Linux
```
- 3: Instale o kedro no ambiente virtual
```
pip install kedro
```

- 4: Crie o projeto kedro mle-kobe
 ```
 kedro new -n mle-kobe -t docs,data --example=n --telemetry=no
 ```
- 5: Volte ao folder principal
 ```
 cd ..
 ``` 
- 6: Mova os arquivos do folder mle-kobe para o folder principal
```
mv mle-kobe/* .
``` 
- 7: Remova o folder mle-kobe
```
rm -rf mle-kobe
``` 
- 8: Renomear requirements.txt para requirements.in
```
mv requirements.txt requirements.in
``` 
- 9: Adicionar dependencias ao requirements.in.
Deve ficar assim:
```
ipython>=8.10
jupyterlab>=3.0
kedro~=0.19.11
kedro-datasets[pandas]
notebook
pyarrow
mlflow<2.13
pycaret[models,mlops]
scikit-optimize
kedro-mlflow
streamlit
```
- 10: Instalar pip-tools e resolver as dependências
  ```
  pip install pip-tools
  pip-compile
  ```
- 11: Instalar as dependencias:
  ```
  pip-sync
  ```

# Desenvolvimento
---
### 2.

Iremos desenvolver um preditor de arremessos usando duas abordagens (regressão e classificação) para prever se o "Black Mamba" (apelido de Kobe) acertou ou errou a cesta.

Baixe os dados de desenvolvimento e produção aqui (datasets: dataset_kobe_dev.parquet e dataset_kobe_prod.parquet). Salve-os numa pasta /data/raw na raiz do seu repositório.

Para começar o desenvolvimento, desenhe um diagrama que demonstra todas as etapas necessárias para esse projeto, desde a aquisição de dados, passando pela criação dos modelos, indo até a operação do modelo.

###INSERIR DIAGRAMA E EXPLICACOES



## 3.
Como as ferramentas Streamlit, MLFlow, PyCaret e Scikit-Learn auxiliam na construção dos pipelines descritos anteriormente? A resposta deve abranger os seguintes aspectos:
- Rastreamento de experimentos;
- Funções de treinamento;
- Monitoramento da saúde do modelo;
- Atualização de modelo;
- Provisionamento (Deployment).

## 4.
Com base no diagrama realizado na questão 2, aponte os artefatos que serão criados ao longo de um projeto. Para cada artefato, a descrição detalhada de sua composição.

## 5.
Implemente o pipeline de processamento de dados com o mlflow, rodada (run) com o nome "PreparacaoDados":
### 5.a) 
Os dados devem estar localizados em "/data/raw/dataset_kobe_dev.parquet" e "/data/raw/dataset_kobe_prod.parquet" 
Observe que há dados faltantes na base de dados! As linhas que possuem dados faltantes devem ser desconsideradas. Para esse exercício serão apenas consideradas as colunas: 
- lat
- lng
- minutes remaining
- period
- playoffs
- shot_distance

A variável shot_made_flag será seu alvo, onde 0 indica que Kobe errou e 1 que a cesta foi realizada. O dataset resultante será armazenado na pasta "/data/processed/data_filtered.parquet". Ainda sobre essa seleção, qual a dimensão resultante do dataset?

Separe os dados em treino (80%) e teste (20 %) usando uma escolha aleatória e estratificada. Armazene os datasets resultantes em "/Data/processed/base_{train|test}.parquet . Explique como a escolha de treino e teste afetam o resultado do modelo final. Quais estratégias ajudam a minimizar os efeitos de viés de dados.
Registre os parâmetros (% teste) e métricas (tamanho de cada base) no MlFlow

![Métricas do dataset](data/08_reporting/metricas_dataset.png)

6
Implementar o pipeline de treinamento do modelo com o MlFlow usando o nome "Treinamento"
  - a)  Com os dados separados para treinamento, treine um modelo com regressão logística do sklearn usando a biblioteca pyCaret.
  - b) Registre a função custo "log loss" usando a base de teste
  - c) Com os dados separados para treinamento, treine um modelo de árvore de decisão do sklearn usando a biblioteca pyCaret.
  - d) Registre a função custo "log loss" e F1_score para o modelo de árvore.
  - e)Selecione um dos dois modelos para finalização e justifique sua escolha.


7
Registre o modelo de classificação e o sirva através do MLFlow (ou como uma API local, ou embarcando o modelo na aplicação). Desenvolva um pipeline de aplicação (aplicacao.py) para carregar a base de produção (/data/raw/dataset_kobe_prod.parquet) e aplicar o modelo. Nomeie a rodada (run) do mlflow como “PipelineAplicacao” e publique, tanto uma tabela com os resultados obtidos (artefato como .parquet), quanto log as métricas do novo log loss e f1_score do modelo.
O modelo é aderente a essa nova base? O que mudou entre uma base e outra? Justifique.
Descreva como podemos monitorar a saúde do modelo no cenário com e sem a disponibilidade da variável resposta para o modelo em operação.
Descreva as estratégias reativa e preditiva de retreinamento para o modelo em operação.
Implemente um dashboard de monitoramento da operação usando Streamlit.