# Estratégia de Crescimento de Receita para Hotel

> Case de Business Analytics utilizando SQL, DuckDB e Python para identificar aproximadamente **R$870 mil** em oportunidades anuais de crescimento de receita por meio da redução de cancelamentos, otimização do ADR e retenção de clientes.

[🇺🇸 English Version](README.md)

---

## Sobre o projeto

Este repositório apresenta um case de Business Analytics desenvolvido a partir de uma base histórica de reservas de hotel entre 2015 e 2017.

O objetivo foi identificar as principais alavancas de receita do negócio e propor iniciativas comercialmente viáveis capazes de aumentar a receita anual em aproximadamente **20%**.

Mais do que uma análise exploratória, este projeto demonstra como transformar dados em decisões estratégicas por meio da construção e validação de hipóteses de negócio.

---

## Problema de negócio

Receita atual

**R$4,97 milhões**

Meta

**R$5,96 milhões**

Gap de crescimento

**≈ R$994 mil**

O projeto responde às seguintes perguntas:

- Onde o hotel está perdendo receita?
- Quais clientes geram maior valor?
- Quais iniciativas devem ser priorizadas considerando impacto e esforço?

---

## Base de dados

Reservas históricas de hotel.

| Métrica | Valor |
|---------|-------:|
| Reservas | 39.859 |
| Período | 2015–2017 |
| Cancelamentos | 27,82% |
| Receita | R$4,97 milhões |

A base contém informações como:

- Canal de reserva
- Antecedência
- Tipo de cliente
- País de origem
- Categoria do quarto
- ADR
- Duração da estadia
- Tipo de depósito
- Pedidos especiais
- Status da reserva

---

## Tecnologias

- Python
- SQL
- DuckDB
- Pandas
- Matplotlib
- Google Colab

---

## Estrutura do repositório

```
hotel-revenue-growth-case/

README.md
README.pt-BR.md

config.py

01_data_exploration.py
02_revenue_diagnosis.py
03_customer_engagement_analysis.py
04_business_recommendations.py
```

---

## Fluxo do projeto

```
Problema de Negócio

↓

Análise Exploratória

↓

Hipóteses

↓

Validação em SQL

↓

Insights

↓

Recomendações

↓

Estimativa de Impacto Financeiro
```

---

## Principais análises

- Diagnóstico de receita
- Análise de cancelamentos
- Performance dos canais de reserva
- Perfil dos clientes
- Clientes recorrentes
- Categorias de quarto
- Sazonalidade
- Engajamento por pedidos especiais

---

## Principais insights

- 27,82% das reservas foram canceladas.
- Aproximadamente R$3,25 milhões em receita potencial foram perdidos.
- Reservas com mais de 90 dias de antecedência concentram a maior parte das perdas.
- O canal direto apresenta menor cancelamento e maior margem líquida.
- Clientes recorrentes cancelam 4,5 vezes menos.
- Quartos premium possuem ADR muito superior, porém baixa participação nas reservas.
- Clientes mais engajados apresentam maior ADR e estadias mais longas.

---

## Recomendações

| Iniciativa | Impacto Estimado |
|------------|----------------:|
| Política de depósito | R$200 mil |
| Upsell pré-chegada | R$180 mil |
| Campanhas de retenção | R$100 mil |
| Estratégia de canal direto | R$150 mil |
| Pacotes de baixa temporada | R$100 mil |
| Programa de fidelidade | R$80 mil |
| Contratos corporativos | R$60 mil |

Impacto potencial total:

**≈ R$870 mil**

Representando aproximadamente **87%** da meta de crescimento proposta.

---

## Próximos passos

- Modelo preditivo de cancelamento
- Simulação de precificação dinâmica
- Customer Lifetime Value (CLV)
- Dashboard interativo
- Previsão de receita
- Sistema de recomendação de upgrades

---

## Autor

**Dante Costa**

Senior Data Analyst

Business Analytics • SQL • Data Strategy • Business Architecture
