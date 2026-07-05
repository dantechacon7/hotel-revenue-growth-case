# Estratégia de Crescimento de Receita para Hotel

> Case de Business Analytics utilizando SQL, DuckDB e Python para identificar aproximadamente **R$1,05 milhão** em oportunidades anuais de crescimento de receita por meio da redução de cancelamentos, otimização de ADR e retenção de clientes.

[🇺🇸 English Version](README.md)

---

## Sobre o projeto

Case de Business Analytics desenvolvido a partir de uma base histórica de reservas de hotel entre 2015 e 2017. O objetivo foi identificar as principais alavancas de receita e propor iniciativas capazes de aumentar a receita anual em aproximadamente **20%**.

---

## Problema de negócio

| | |
|---|---|
| Receita atual | **R$11,60 milhões** |
| Meta (+20%) | **R$13,92 milhões** |
| Gap de crescimento | **≈ R$2,32 milhões** |

- Onde o hotel está perdendo receita?
- Quais clientes geram maior valor?
- Quais iniciativas priorizar considerando impacto e esforço?

---

## Base de dados

| Métrica | Valor |
|---------|------:|
| Reservas | 39.859 |
| Período | 2015–2017 |
| Taxa de cancelamento | 27,82% |
| Receita realizada | R$11,60M |
| Receita perdida (cancelamentos) | R$5,84M |
| Diária média (ADR) | R$91,29 |

Atributos: canal de reserva, antecedência, tipo de cliente, país, categoria do quarto, ADR, duração da estadia, tipo de depósito, pedidos especiais, status da reserva.

---

## Tecnologias

Python · SQL · DuckDB · Pandas · Matplotlib · Google Colab

---

## Estrutura do repositório

```
hotel-revenue-growth-case/
├── README.md
├── README.pt-BR.md
├── config.py
├── 01_data_exploration.py
├── 02_revenue_diagnosis.py
├── 03_customer_engagement_analysis.py
├── 04_business_recommendations.py
└── gold_analytics_fct_hotel_reservations.ipynb
```

---

## Principais insights

**Cancelamento:** 27,82% das reservas canceladas → R$5,84M perdidos. Reservas com 90+ dias de antecedência: 40% do volume, 64% da receita perdida. Sem custo de cancelamento, o hóspede reserva sem compromisso real.

**Canal Direto:** Menor cancelamento (13,48%), ADR R$111,67, sem comissão OTA. Melhor canal por receita líquida por reserva iniciada.

**Anomalia no pgto não reembolsável:** 96% de cancelamento — concentrado em grupos portugueses. Assimetria cambial euro/real torna o depósito em reais uma barreira irrisória.

**Clientes recorrentes:** 4,4% da base, cancelam 4,5× menos. Recorrentes de FDS atingem ADR R$155–222 com ~6 noites em meses de pico.

**Engajamento:** Cada pedido especial adicional = +R$20–30 ADR, +0,3 noites, independente de sazonalidade. HB + 3 pedidos: R$168 ADR, 9% cancelamento. FB + 3 pedidos: 0% cancelamento.

---

## Recomendações

| # | Iniciativa | Impacto Est. | Esforço | Prazo |
|---|-----------|-------------:|---------|-------|
| 1 | Política de depósito >30 dias (exceto Grupos) | ~R$380k | Baixo | Imediato |
| 2 | Upsell pré-chegada (quarto + alimentação + engajamento) | ~R$180k | Baixo | Imediato |
| | **Subtotal imediato** | **~R$560k (24%)** | | |
| 3 | Gestão de demanda (retenção + baixa temporada) | ~R$200k | Médio | 1–2 meses |
| 4 | Migração canal Direto | ~R$150k | Médio | 3–6 meses |
| | **Subtotal curto/médio prazo** | **~R$910k (39%)** | | |
| 5 | Retenção e fidelização (fidelidade + corporativo) | ~R$140k | Médio/Alto | 3–12 meses |
| | **Total acumulado** | **~R$1,05M (45%)** | | |

Atingir 100% da meta exige alavancas fora do escopo dos dados: precificação dinâmica, novos mercados ou expansão de capacidade.

---

## Nota metodológica

**Bug de receita (corrigido):** O dataset original usa vírgula como separador decimal em `receita_por_noite`. Sessões anteriores subestimavam a receita em ~2,34×. Correção: `str.replace(',', '.')` antes do cast para float. Ver `config.py`.

---

## Próximos passos

Modelo preditivo de cancelamento · Simulação de precificação dinâmica · Customer Lifetime Value · Dashboard interativo

---

## Autor

**Dante Costa** — Senior Data Analyst
Business Analytics · SQL · Data Strategy · Business Architecture
