## Configurando ambiente com DuckDB no colab

!pip install -q duckdb

from google.colab import files

files.upload()

import duckdb

con = duckdb.connect()

## Setup da tabela fato

!pip install duckdb -q
import duckdb, pandas as pd

df = pd.read_excel('Case_Hotel_BA_.xlsx', sheet_name='Base de Dados')
df['receita_total'] = df['receita_por_noite'] * (df['nro_noites_fds'] + df['nro_noites_dds'])
df['total_noites'] = df['nro_noites_fds'] + df['nro_noites_dds']

con = duckdb.connect()
con.register('reservas', df)

## Criando receita_total - ausente do CSV
con.sql("""
CREATE OR REPLACE TABLE fct_hotel_reservations AS
SELECT *, TRY_CAST(receita_por_noite AS DOUBLE)*(nro_noites_fds+nro_noites_dds) AS receita_total,
(nro_noites_fds+nro_noites_dds) AS total_noites
FROM fct_hotel_reservations
""")

## Normalizando com try_cast algumas colunas
con.sql("""
CREATE OR REPLACE TABLE fct_hotel_reservations AS
SELECT * REPLACE(
  TRY_CAST(reserva_cancelada AS INT) AS reserva_cancelada,
  TRY_CAST(receita_por_noite AS DOUBLE) AS receita_por_noite
),
TRY_CAST(receita_por_noite AS DOUBLE)*(nro_noites_fds+nro_noites_dds) AS receita_total,
(nro_noites_fds+nro_noites_dds) AS total_noites
FROM fct_hotel_reservations
""")
