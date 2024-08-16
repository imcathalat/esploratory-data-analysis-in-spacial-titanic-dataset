# Project for honors on Exploratory Data Analysis IBM Course

## Objetivo

Identificar padrões no dataset que me permita **inferir sobre os motivos de um passageiro ter sido aciedentalmente transportado pra outra dimensão** por efeito da colisão da nave com uma nuvem de poeira.

## Steps Summary

#### Identificar distribuição dos dados

- Teste de Shapiro-Wilk ou Kolmogorov-Smirnov
- Q-Q Plot (Gráfico de Probabilidade Quantil-Quantil)

#### Tratar Duplicated Data

- Data Filtering
- Drop duplicated values
  
#### Tratar Missing Data

- Data Filtering
- Drop missing values
- Input mean values in missing values

#### Tratar Outliers

- Z-Score
- Boxplot

#### Identificar Correlação entre as features e visualizar tal correlação

- Pair plots
- Scatter plots
- Heat Maps
- Correlation Matrixes
- corr() function
- Regressão Linear Simples
- Análise de Resíduos
- Agrupamento de dados
- Data Filtering
- pairplot.express pandas library

#### Normalizar Dados

- Box-Cox Transform: work with skewed data
- Log Transformation
 
#### Feature Scalling

- MinMax Scalling
- Standard Scalling

#### Feature Encoding

- Binary Enconding
- One-hot Encoding
- Ordinal Enconding

#### Revisar correlação de dados para verificar se ainda existe

- Pair plots
- Scatter plots
- Heat Maps
- Correlation Matrixes
- corr() function
- Regressão Linear Simples
- Análise de Resíduos

#### Tratar dados utilizando Polynomial Syntax se identificar necessidade

#### Revisar se Polynomial Syntax foi aplicada corretamente

#### Identificação das 3 hipóteses

- Identificar Distribuição
- Identificar as hipóteses
- Identificar Nível de Significância (α)
- Cálculo Estatístico do Teste (LikeliHood Ratio Test)
- Cálculo do p-valor para afirmar ou refutrar hipótese nula


# Start EDA

## Duplicated Values

```python
duplicated_data = initial_df[initial_df.duplicated(['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'Name', 'Transported'])]
duplicated_data.head()

initial_df.index.is_unique
True
```

O comportamento do método .head() ao mostrar nenhum dado duplicado e o retorno True da afirmativa is_unique identifica que não há dados duplicados no dataset.

## Missing Values
```python
total_null = initial_df.isnull().sum>sort_values(ascending=False)
total_null

total_null.plot(kind="bar", figsize = (8, 6), fontsize = 10)
plt.xlabel("Features", fontsize = 20)
plt.ylabel("Count", fontsize = 20)
plt.title("Total Missing Values", fontsize = 20)
```
Gráfico quantos valores nulos há em cada conjunto de variáveis.
